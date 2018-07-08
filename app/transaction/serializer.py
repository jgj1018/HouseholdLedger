from rest_framework import serializers
from transaction.models import Transaction

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