from django.test import TestCase, override_settings, modify_settings
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Budget
from home.tests import register, login
from .filter import BudgetFilter
from django.contrib.auth.models import User

# Create your tests here.

@modify_settings(MIDDLEWARE={
    'remove': 'middleware.authCheck.JwtExpiCheck',
})
class BudgetTest(APITestCase):
    key=None
    client = APIClient()
    def setUp(self):
        register()
        self.key= login()
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.key)


    @override_settings(REST_USE_JWT=True)
    def test_create_budget(self):
        self.assertEqual(Budget.objects.count(), 0)

        url = reverse('budget:budget-list')
        data = {
            # "user": User.objects.first().id,
            "cost_amount": 100,
            "budget_type": "07"
        }
        # self.client.force_login(User.objects.first())
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        list_url = reverse('budget:budget-list')
        list_resp = self.client.get(list_url)
        self.assertEqual(len(list_resp.data), 0)

        data = {
            "cost_amount": 100,
            "budget_type": "01"
        }
        resp2 = self.client.post(url, data, format='json')
        self.assertEqual(resp2.status_code,
                         status.HTTP_201_CREATED)

        self.assertEqual(Budget.objects.get().budget_type, '01')
        list_resp2 = self.client.get(list_url)
        self.assertEqual(len(list_resp2.data), 1)


    @override_settings(REST_USE_JWT=True)
    def test_filter_budget(self):
        url = reverse('budget:budget-list')
        data = {

            "cost_amount": 100,
            "budget_type": "01"
        }
        response = self.client.get(url, data= data, status_code=201)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        putresp = self.client.post(url, data= data, status_code=201)
        self.assertEqual(putresp.status_code, status.HTTP_201_CREATED)
        new_response = self.client.get(url, data= data, status_code=201)
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(new_response.data), 1)
        user = User.objects.create(username='name', email='test@email.com')
        Budget.objects.create(
            user_id = user.id,
            cost_amount =100,
            budget_type = '01'
        )
        self.assertEqual(Budget.objects.count(), 2)
        response2 = self.client.get(url, data= data, status_code=201)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response2.data), 1)

    def test_filter_set(self):
        import datetime

        url = reverse('budget:budget-list')
        data = {
            "user": User.objects.first().id,
            "cost_amount": 100,
            "budget_type": "01"

        }
        response = self.client.post(url, data, status_code=201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        qs = Budget.objects.all()
        self.assertTrue(len(qs) == 1)
        f1 = BudgetFilter({'updated_at_before': '2018-08-10', 'updated_at_after': '2018-08-01'})
        self.assertTrue(len(f1.qs) == 0)
        today = datetime.date.today().strftime("%Y-%m-%d")
        f2 = BudgetFilter({'updated_at_before': today, 'updated_at_after': today})
        self.assertTrue(len(f2.qs) == 1)

    @override_settings(REST_USE_JWT=True)
    def test_filter_range_budget(self):
        url = reverse('budget:budget-list')
        data = {
            "user": User.objects.first().id,
            "cost_amount": 100,
            "budget_type": "01",
            'budget_name': 'test'
        }
        putresp = self.client.post(url, data= data, status_code=201)
        self.assertEqual(putresp.status_code, status.HTTP_201_CREATED)
        new_response = self.client.get(url, data= data, status_code=201)
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(new_response.data), 1)

        data['updated_at_before'] = '2018-08-10',
        data['updated_at_after'] = '2018-08-01',

        response2 = self.client.get(url, data= data, status_code=201)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response2.data), 0)

