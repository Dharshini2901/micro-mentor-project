from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser

class UserRegistrationTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_mentor_user(self):
        user = CustomUser.objects.create_user(
            username='test_mentor',
            email='mentor@test.com',
            password='test1234',
            role='mentor'
        )
        self.assertEqual(user.username, 'test_mentor')
        self.assertEqual(user.role, 'mentor')
        self.assertTrue(user.check_password('test1234'))

    def test_create_mentee_user(self):
        user = CustomUser.objects.create_user(
            username='test_mentee',
            email='mentee@test.com',
            password='test1234',
            role='mentee'
        )
        self.assertEqual(user.role, 'mentee')

    def test_user_str(self):
        user = CustomUser.objects.create_user(
            username='dharshini',
            password='test1234',
            role='mentor'
        )
        self.assertEqual(str(user), 'dharshini')

    def test_login_page_loads(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials(self):
        CustomUser.objects.create_user(
            username='loginuser',
            password='test1234',
            role='mentor'
        )
        response = self.client.post('/accounts/login/', {
            'username': 'loginuser',
            'password': 'test1234'
        })
        self.assertIn(response.status_code, [200, 302])

    def test_login_with_invalid_credentials(self):
        response = self.client.post('/accounts/login/', {
            'username': 'wronguser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
