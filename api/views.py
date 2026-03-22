from rest_framework.decorators import api_view
from rest_framework.response import Response
from mentors.models import MentorProfile
from .serializers import MentorSerializer

@api_view(['GET'])
def mentor_list(request):
    mentors = MentorProfile.objects.all()
    serializer = MentorSerializer(mentors, many=True)
    return Response(serializer.data)
