from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message
from django.contrib.auth.decorators import login_required

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'chat/send_message.html', {'form': form})

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'chat/inbox.html', {'messages': messages})
