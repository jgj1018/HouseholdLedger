from rest_framework import serializers
from transaction.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.RelatedField
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Transaction
        fields = ('user',
                  'transaction_id',
                  'transaction_name',
                  'cost_amount',
                  'credit_type',
                  'debit_type',
                  'created_at',
                  'updated_at',
                  )


