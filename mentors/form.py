from django import forms
from .models import MentorProfile
from .models import Booking

class MentorProfileForm(forms.ModelForm):
    class Meta:
        model = MentorProfile
        fields = ['bio', 'expertise', 'hourly_rate']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['mentor', 'date', 'time']


