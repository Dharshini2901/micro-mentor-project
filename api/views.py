from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from mentors.models import MentorProfile, Booking
from accounts.models import CustomUser
from .serializers import MentorSerializer, BookingSerializer, UserSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def mentor_list(request):
    mentors = MentorProfile.objects.all()
    serializer = MentorSerializer(mentors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def mentor_detail(request, pk):
    try:
        mentor = MentorProfile.objects.get(pk=pk)
    except MentorProfile.DoesNotExist:
        return Response({'error': 'Mentor not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MentorSerializer(mentor)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def booking_list(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
