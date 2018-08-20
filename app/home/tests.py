from django.test import TestCase, override_settings, modify_settings
from rest_framework import status
from rest_framework.test import  APIClient
from transaction.models import Transaction
from .globals import functions
import time
from django.contrib.auth.models import User


@modify_settings(MIDDLEWARE={
    'remove': 'middleware.authCheck.JwtExpiCheck',
})
def register():
    client = APIClient()

    resp = client.post('/account/registration/', data=APIBasicTests.REGISTRATION_DATA, status_code=200)
    assert resp.status_code == status.HTTP_201_CREATED

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
        register()

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

    @override_settings(REST_USE_JWT=True)
    def test_refresh_token(self):
      payload = {
        "email": self.EMAIL,
        "username": self.USERNAME,
        "password": self.PASS
      }
      resp = self.client.post('/account/login/', data=payload, status_code=200)
      token = resp.data['token']
      resp2 = self.client.get('/boot/', **{'HTTP_AUTHORIZATION': 'Bearer'+token})
      self.assertEqual(status.HTTP_200_OK, resp2.status_code)
      for i in range(0, 5):
          token = resp2.data['token']
          resp3 = self.client.get('/boot/', **{'HTTP_AUTHORIZATION': 'Bearer'+token})
          self.assertEqual(status.HTTP_200_OK, resp3.status_code)
          time.sleep(5)
          resp2 = resp3


class GlobalObjTest(TestCase):

    def test_filter_by_user_id_query_has_where_user_id(self):
        query_set = functions.filter_by_user_id(Transaction.objects, {'user': 1})
        query = query_set.query.__str__()
        self.assertIn('WHERE', query)

        self.assertIn('"user_id" = ', query)
