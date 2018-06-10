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
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from django.contrib.auth.models import User
import time

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
        payload = {
            "email": self.EMAIL,
            "username": self.USERNAME,
            "password": self.PASS
        }

        resp1 = self.client.post('/account/registration/', data=self.REGISTRATION_DATA, status_code=200)
        pass

    @override_settings(REST_USE_JWT=True)
    def test_login_jwt(self):
        payload = {
            "email": self.EMAIL,
            "username": self.USERNAME,
            "password": self.PASS
        }

        resp = self.client.post('/account/login/', data=payload, status_code=200)
        self.assertEqual('token' in resp.data.keys(), True)
        time.sleep(10)

        token = resp.data['token']
        data = {'token': token}
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        user = valid_data['user']
        re_token = self.client.post('/refresh-token/',data=data)
        refreshed = re_token.data['token']
        re_data = {'token': refreshed}
        time.sleep(10)
        re_valid_data = VerifyJSONWebTokenSerializer().validate(re_data)
        re_user = re_valid_data['user']
        self.assertTrue(isinstance(re_user, User))

    @override_settings(REST_USE_JWT=True)
    def test_refresh_token(self):
      payload = {
        "email": self.EMAIL,
        "username": self.USERNAME,
        "password": self.PASS
      }
      resp = self.client.post('/account/login/', data=payload, status_code=200)
      token = resp.data['token']
      data = {'token': token}
      resp2 = self.client.get('/boot/', data= data)
      self.assertEqual(200, resp2.status_code)
      for i in range(0, 5):
          token = resp2.data['token']
          data2 = {'token': token}
          resp3 = self.client.get('/boot/', data= data2)
          self.assertEqual(200, resp3.status_code)
          time.sleep(5)
          resp2 = resp3

