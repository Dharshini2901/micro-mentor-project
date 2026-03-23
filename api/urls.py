from django.urls import path
from . import views

urlpatterns = [
    path('mentors/', views.mentor_list, name='mentor-list'),
    path('mentors/<int:pk>/', views.mentor_detail, name='mentor-detail'),
    path('bookings/', views.booking_list, name='booking-list'),
    path('users/', views.user_list, name='user-list'),
]
