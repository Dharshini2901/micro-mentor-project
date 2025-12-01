from django.urls import path
from .views import create_mentor_profile, mentor_list, book_mentor ,my_bookings,confirm_booking # <-- make sure book_mentor is imported

urlpatterns = [
    path("create-profile/", create_mentor_profile, name="create_mentor_profile"),
    path('list/', mentor_list, name='mentor_list'),
    path('book/', book_mentor, name='book_mentor'),
    path('my-bookings/', my_bookings, name='my_bookings'),
    path('confirm/<int:booking_id>/', confirm_booking, name='confirm_booking')


]
