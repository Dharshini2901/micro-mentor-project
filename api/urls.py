from django.urls import path
from . import views

urlpatterns = [
    path('mentors/', views.mentor_list, name='mentor-list'),
]
