from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('mentors/', views.mentor_list, name='mentor-list'),
    path('mentors/<int:pk>/', views.mentor_detail, name='mentor-detail'),
    path('bookings/', views.booking_list, name='booking-list'),
    path('users/', views.user_list, name='user-list'),
    path('login/', obtain_auth_token, name='api-login'),
]
