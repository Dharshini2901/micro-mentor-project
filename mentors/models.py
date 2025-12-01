from django.db import models
from django.conf import settings  # Required for AUTH_USER_MODEL
from accounts.models import CustomUser

class MentorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='mentor_profile')
    bio = models.TextField()
    expertise = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.expertise}"


class Booking(models.Model):
    mentor = models.ForeignKey(MentorProfile, on_delete=models.CASCADE)
    mentee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default="pending")
    confirmed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="confirmed_bookings"
    )  

    def __str__(self):
        return f"{self.mentee} booked {self.mentor} on {self.date} at {self.time}"
