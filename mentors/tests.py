from django.test import TestCase
from accounts.models import CustomUser
from mentors.models import MentorProfile, Booking
import datetime

class MentorProfileTest(TestCase):

    def setUp(self):
        self.mentor_user = CustomUser.objects.create_user(
            username='arjun_test',
            email='arjun@test.com',
            password='test1234',
            role='mentor'
        )
        self.mentor_profile = MentorProfile.objects.create(
            user=self.mentor_user,
            bio='Experienced Django developer.',
            expertise='Python, Django',
            hourly_rate=60.00
        )
        self.mentee_user = CustomUser.objects.create_user(
            username='priya_test',
            email='priya@test.com',
            password='test1234',
            role='mentee'
        )

    def test_mentor_profile_created(self):
        self.assertEqual(self.mentor_profile.expertise, 'Python, Django')
        self.assertEqual(self.mentor_profile.hourly_rate, 60.00)

    def test_mentor_profile_str(self):
        self.assertEqual(
            str(self.mentor_profile),
            'arjun_test - Python, Django'
        )

    def test_booking_created(self):
        booking = Booking.objects.create(
            mentor=self.mentor_profile,
            mentee=self.mentee_user,
            date=datetime.date.today(),
            time=datetime.time(10, 0),
            status='pending'
        )
        self.assertEqual(booking.status, 'pending')
        self.assertEqual(booking.mentor, self.mentor_profile)
        self.assertEqual(booking.mentee, self.mentee_user)

    def test_booking_str(self):
        booking = Booking.objects.create(
            mentor=self.mentor_profile,
            mentee=self.mentee_user,
            date=datetime.date(2026, 3, 23),
            time=datetime.time(10, 0),
            status='pending'
        )
        self.assertIn('arjun_test', str(booking))
        self.assertIn('priya_test', str(booking))
