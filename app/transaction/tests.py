from django.test import TestCase, override_settings, modify_settings
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from transaction.models import Budget
from home.tests import register
# Create your tests here.

@modify_settings(MIDDLEWARE={
    'remove': 'middleware.authCheck.JwtExpiCheck',
})
class BudgetTest(APITestCase):

    def setUp(self):
        register()
        pass

    @override_settings(REST_USE_JWT=True)
    def test_create_budget(self):

        url = reverse('asset:budget-list')
        data = {
            "user": 1,
            "amount": 100,
            "budget_type": "07"
        }
        response = self.client.post(url, data= data, status_code=201)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Budget.objects.count(), 0)
        data = {
            "user": 1,
            "amount": 100,
            "budget_type": "03"
        }
        resp2 = self.client.post(url, data= data, status_code=201)
        self.assertEqual(resp2.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Budget.objects.get().budget_type, '03')