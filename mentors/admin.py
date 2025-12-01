from django.contrib import admin
from .models import MentorProfile, Booking

@admin.register(MentorProfile)
class MentorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'expertise', 'hourly_rate')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('mentee', 'mentor', 'date', 'time', 'status')
    list_filter = ('status', 'date')
