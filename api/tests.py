from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import CustomUser
from mentors.models import MentorProfile

class MentorAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.mentor_user = CustomUser.objects.create_user(
            username='api_mentor',
            email='api@test.com',
            password='test1234',
            role='mentor'
        )
        self.mentor_profile = MentorProfile.objects.create(
            user=self.mentor_user,
            bio='Test bio',
            expertise='Python, Django',
            hourly_rate=60.00
        )

    def test_mentor_list_returns_200(self):
        response = self.client.get('/api/mentors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_mentor_list_returns_data(self):
        response = self.client.get('/api/mentors/')
        self.assertEqual(len(response.data), 1)

    def test_mentor_detail_returns_200(self):
        response = self.client.get(f'/api/mentors/{self.mentor_profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_mentor_detail_returns_correct_data(self):
        response = self.client.get(f'/api/mentors/{self.mentor_profile.id}/')
        self.assertEqual(response.data['username'], 'api_mentor')
        self.assertEqual(response.data['expertise'], 'Python, Django')

    def test_mentor_detail_404(self):
        response = self.client.get('/api/mentors/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_booking_list_returns_200(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list_returns_200(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
