from django.test import TestCase, override_settings
from django.contrib.auth import get_user_model
from django.core import mail
from django.conf import settings
from django.utils.encoding import force_text

from allauth.account import app_settings as account_app_settings
from rest_framework import status
from rest_framework.test import APIRequestFactory

from rest_auth.registration.views import RegisterView
from rest_auth.registration.app_settings import register_permission_classes

from django.urls import reverse


class APIBasicTests(TestCase):
    """
    Case #1:
    - user profile: defined
    - custom registration: backend defined
    """

    # urls = 'tests.urls'

    USERNAME = 'admin'
    PASS = 'gring21!'
    EMAIL = "admin@admin.com"
    NEW_PASS = 'new-test-pass'
    REGISTRATION_VIEW = 'rest_auth.runtests.RegistrationView'

    # data without user profile
    REGISTRATION_DATA = {
        "username": USERNAME,
        "email":EMAIL,
        "password1": PASS,
        "password2": PASS
    }

    REGISTRATION_DATA_WITH_EMAIL = REGISTRATION_DATA.copy()
    REGISTRATION_DATA_WITH_EMAIL['email'] = EMAIL

    BASIC_USER_DATA = {
        'first_name': "John",
        'last_name': 'Smith',
        'email': EMAIL
    }
    USER_DATA = BASIC_USER_DATA.copy()
    USER_DATA['newsletter_subscribe'] = True

    def setUp(self):
        pass

    @override_settings(REST_USE_JWT=True)
    def test_login_jwt(self):
        payload = {
            "email": self.EMAIL,
            "username": self.USERNAME,
            "password": self.PASS
        }

        resp1 = self.client.post('/account/registration/', data=self.REGISTRATION_DATA, status_code=200)
        self.assertEqual(201, resp1.status_code)
        resp = self.client.post('/account/login/', data=payload, status_code=200)

        self.assertEqual('token' in resp.data.keys(), True)

