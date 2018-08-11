from django.test import TestCase, override_settings, modify_settings
from rest_framework.test import APITestCase
from rest_framework import status
from django.shortcuts import resolve_url
from .models import Transaction
from home.tests import register

@modify_settings(MIDDLEWARE={
    'remove': 'middleware.authCheck.JwtExpiCheck',
})
class TransactionTest(APITestCase):


    def setUp(self):
        register()
        pass

    @override_settings(REST_USE_JWT=True)
    def test_create_transaction_success(self):
        '''normal success case'''
        url = resolve_url('/transaction/transaction/')
        data = {
            "user": 1,
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
            "debit_type": "1",
            "cost_amount": 1000
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when transaction_name parameter doesn't exist'''
        data = {
            "user": 1,
            "credit_type": "1",
            "debit_type": "1",
            "cost_amount": 1000
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when credit_type parameter doesn't exist'''
        data = {
            "user": 1,
            "transaction_name": "test",
            "debit_type": "1",
            "cost_amount": 1000
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when debit_type parameter doesn't exist'''
        data = {
            "user": 1,
            "transaction_name": "test",
            "credit_type": "1",
            "cost_amount": 1000
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when cost_amount parameter doesn't exist'''
        data = {
            "user": 1,
            "transaction_name": "test",
            "credit_type": "1",
            "debit_type": "1",
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

        '''when credit_type is string'''
        data = {
          "user": 1,
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
          "user": 1,
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
            "user": 1,
            "transaction_name": 'test',
            "credit_type": "1",
            "debit_type": "1",
            "cost_amount": 'test'
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Transaction.objects.count(), 1)

