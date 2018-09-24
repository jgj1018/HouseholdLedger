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
        url = reverse('transaction:transaction-list')


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
    def test_filter_range_transaction(self):
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


    @override_settings(REST_USE_JWT=True)
    def test_update_transaction(self):
        create_url = reverse('transaction:transaction-list')
        data = {

            "transaction_name": "test",
            "credit_type": 1,
            "debit_type": 1,
            "cost_amount": 1000
        }
        postresp = self.client.post(create_url, data=data, status_code=201)
        self.assertEqual(postresp.status_code, status.HTTP_201_CREATED)

        first_transaction = Transaction.objects.first()
        update_url = reverse('transaction:transaction-detail', kwargs={'pk': first_transaction.transaction_id})
        update_data = {
            'transaction_name': 'test22'
        }
        putresp = self.client.patch(update_url, data=update_data, status_code=status.HTTP_200_OK)
        updated_first_transaction = Transaction.objects.first()
        self.assertEqual('test22', updated_first_transaction.transaction_name)

        new_register_id = {
        "username": 'username',
        "email": 'user@name.com',
        "password1": 'gring21!',
        "password2": 'gring21!'
        }

        resp = self.client.post('/account/registration/', data=new_register_id, status_code=200)
        new_login_data = {
            "username": 'username',
            "email": 'user@name.com',
            "password": 'gring21!',
        }
        log_out_resp = self.client.post('/account/logout', status_code=200)

        login_resp = self.client.post('/account/login/', data=new_login_data, status_code=200)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + login_resp.data['token'])
        fail_update_url = reverse('transaction:transaction-detail', kwargs={'pk': first_transaction.transaction_id})
        fail_update_data = {
            'transaction_name': 'fail'
        }
        fail_resp = self.client.patch(fail_update_url, data=fail_update_data, status_code=status.HTTP_200_OK)
        self.assertEqual(fail_resp.status_code, status.HTTP_404_NOT_FOUND)
