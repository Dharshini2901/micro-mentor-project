from rest_framework import serializers
from mentors.models import MentorProfile, Booking
from accounts.models import CustomUser

class MentorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = MentorProfile
        fields = ['id', 'username', 'email', 'bio', 'expertise', 'hourly_rate']

class BookingSerializer(serializers.ModelSerializer):
    mentor_name = serializers.CharField(source='mentor.user.username', read_only=True)
    mentee_name = serializers.CharField(source='mentee.username', read_only=True)
    class Meta:
        model = Booking
        fields = ['id', 'mentor', 'mentor_name', 'mentee', 'mentee_name', 'date', 'time', 'status']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']
