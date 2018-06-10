from django.contrib.auth.models import User, Group
from rest_framework import serializers
from home.models import Transaction


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url',
                  'username',
                  'email',
                  'groups'
                  )

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('user_id',
                  'transaction_id',
                  'transaction_name',
                  'cost_amount',
                  'transaction_type',
                  'created_at',
                  'updated_at',
                  )
