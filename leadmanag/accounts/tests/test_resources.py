import json
from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from accounts.resources import (
    RegisterView, LoginView, UserView
)


class RegisterTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory()
        User.objects.create_user(
            username='super',
            email='super@super.com',
            password='123',
        )

    def test_create_correct_return(self):
        new_user = {
            'username': 'ademir',
            'email': 'ademir@gmail.com',
            'password': '12345',
        }
        request = self.request.post(
            reverse('register'),
            json.dumps(new_user),
            content_type='application/json'
        )
        response = RegisterView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.data.keys()), ['user', 'token'])


class LoginTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory()
        User.objects.create_user(
            username='super',
            email='super@super.com',
            password='123',
        )

    def test_login_correct_return(self):
        registered_user = {
            'username': 'super',
            'password': '123',
        }
        request_login = self.request.post(
            reverse('login'),
            json.dumps(registered_user),
            content_type='application/json'
        )
        response_login = LoginView.as_view()(request_login)

        self.assertEqual(response_login.status_code, 200)
        self.assertEqual(list(response_login.data.keys()), ['user', 'token'])


class UserTestCase(TestCase):

    def setUp(self):
        self.request = RequestFactory()
        User.objects.create_user(
            username='super',
            email='super@super.com',
            password='123',
        )

    def test_user_access_only_if_loged(self):
        request = self.request.get(reverse('user'))
        response = UserView.as_view()(request)
        self.assertNotEqual(response.status_code, 200)
