from rest_framework import serializers
from transaction.models import Transaction
from home.globals.const import *

class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.RelatedField
    credit_type = serializers.SerializerMethodField()
    debit_type = serializers.SerializerMethodField()
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
    def get_credit_type(self, obj):
        if obj.credit_type == 1:
            return credit_type[0]['name']
        elif obj.credit_type == 2:
            return credit_type[1]['name']
        elif obj.credit_type == 3:
            return credit_type[2]['name']

    def get_debit_type(self, obj):
        if obj.credit_type == 1:
            return debit_type[0]['name']
        elif obj.credit_type == 2:
            return debit_type[1]['name']
        elif obj.credit_type == 3:
            return debit_type[2]['name']








