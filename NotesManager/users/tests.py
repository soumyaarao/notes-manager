from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomUser

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-registration')
        self.login_url = reverse('user-login')
        self.user_data = {'username': 'testuser', 'password': 'testpassword'}

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, 'testuser')

    def test_user_login(self):
        # Register user
        self.client.post(self.register_url, self.user_data, format='json')

        # Login user
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_user_login(self):
        # Try logging in with incorrect credentials
        response = self.client.post(self.login_url, {'username': 'nonexistent', 'password': 'invalid'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
