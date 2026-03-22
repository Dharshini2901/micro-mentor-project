from rest_framework import serializers
from mentors.models import MentorProfile

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfile
        fields = '__all__'
