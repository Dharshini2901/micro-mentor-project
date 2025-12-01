from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mentors.form import MentorProfileForm, BookingForm
from .models import MentorProfile, Booking
from accounts.models import CustomUser
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def create_mentor_profile(request):
    # Only mentors can access
    if request.user.role != 'mentor':
        return redirect('dashboard')  

    # Check if mentor already created a profile
    if MentorProfile.objects.filter(user=request.user).exists():
        return render(request, 'mentors/already_created.html')  

    # If mentor has no profile → show form
    if request.method == 'POST':
        form = MentorProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')
    else:
        form = MentorProfileForm()

    return render(request, 'mentors/create_profile.html', {'form': form})



# MENTOR LIST (PUBLIC PAGE)
@login_required
def mentor_list(request):
    mentors = MentorProfile.objects.all()
    return render(request, 'mentors/mentor_list.html', {'mentors': mentors})



# BOOK MENTOR
@login_required
def book_mentor(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.mentee = request.user
            booking.save()
            return redirect('my_bookings')
    else:
        form = BookingForm()

    return render(request, 'mentors/book_mentor.html', {'form': form})


# MY BOOKINGS (MENTEE DASHBOARD)
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(mentee=request.user).order_by('-date', '-time')

    return render(request, 'mentors/my_bookings.html', {
        'bookings': bookings,
        
    })

@login_required
def confirm_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    # Only the mentor of this booking can confirm
    if booking.mentor.user != request.user:
        return redirect('dashboard')  

    if request.method == "POST":
        booking.status = "confirmed"
        booking.confirmed_by = request.user
        booking.save()
        return redirect('dashboard')

    return render(request, 'mentors/confirm_booking.html', {'booking': booking})