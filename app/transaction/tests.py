from django.test import override_settings, modify_settings
from rest_framework.test import APITestCase, APIClient
from django.shortcuts import resolve_url
from rest_framework import status
from django.urls import reverse
from .models import Transaction
from home.tests import register, login
from django.contrib.auth.models import User


@modify_settings(MIDDLEWARE={
    'remove': 'middleware.authCheck.JwtExpiCheck',
})
class TransactionTest(APITestCase):


    key=None
    client = APIClient()
    def setUp(self):
        register()
        self.key= login()
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.key)

    @override_settings(REST_USE_JWT=True)
    def test_create_transaction_success(self):
        '''normal success case'''
        url = resolve_url('/transaction/transaction/')
        data = {

            "transaction_name": "test",
            "credit_type": "1",
            "debit_type": "1",
            "cost_amount": 1000
        }
        res = self.client.post(url, data= data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when user parameter doesn't exist'''
        data = {
            "transaction_name": "test",
            "credit_type": "1",
#            "debit_type": "10",
            "cost_amount": 1000
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when transaction_name parameter doesn't exist'''
        data = {

            "credit_type": "1",
            "debit_type": "1",
            "cost_amount": 1000
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when credit_type parameter doesn't exist'''
        data = {

            "transaction_name": "test",
            "debit_type": "1",
            "cost_amount": 1000
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when debit_type parameter doesn't exist'''
        data = {

            "transaction_name": "test",
            "credit_type": "1",
            "cost_amount": 1000
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when cost_amount parameter doesn't exist'''
        data = {

            "transaction_name": "test",
            "credit_type": "1",
            "debit_type": "1",
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when credit_type is string'''
        data = {

          "transaction_name": 'test',
          "credit_type": "test",
          "debit_type": "1",
          "cost_amount": 1000
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when debit_type is string'''
        data = {

          "transaction_name": 'test',
          "credit_type": "1",
          "debit_type": "test",
          "cost_amount": 1000
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when cost_amount is string'''
        data = {

            "transaction_name": 'test',
            "credit_type": "1",
            "debit_type": "1",
            "cost_amount": 'test'
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

    @override_settings(REST_USE_JWT=True)
    def test_filter_range_budget(self):
        url = reverse('transaction:transaction-list')
        data = {

            "transaction_name": "test",
            "credit_type": 1,
            "debit_type": 1,
            "cost_amount": 1000
        }
        putresp = self.client.post(url, data=data, status_code=201)
        self.assertEqual(putresp.status_code, status.HTTP_201_CREATED)

        new_response = self.client.get(url, data= data, status_code=201)
        self.assertEqual(new_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(new_response.data), 1)

        data['updated_at_before'] = '2018-08-10',
        data['updated_at_after'] = '2018-08-01',
        response2 = self.client.get(url, data= data, status_code=201)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response2.data), 0)


