from rest_framework import serializers
from transaction.models import Transaction
from home.globals.const import *
from rest_framework.settings import api_settings

class TransactionSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    credit_type = serializers.IntegerField(required=True)
    debit_type = serializers.IntegerField(required=True)
    created_at = serializers.DateTimeField(required=False, read_only=True, format=api_settings.DATETIME_FORMAT)
    updated_at = serializers.DateTimeField(required=False)


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

    def to_representation(self, instance):
        ret =  super().to_representation(instance)
        ret['credit_type'] = self.__get_credit_type(instance)
        ret['debit_type'] = self.__get_debit_type(instance)

        return ret
    def __get_credit_type(self, obj):
        if obj.credit_type == 1:
            return credit_type[0]['name']
        elif obj.credit_type == 2:
            return credit_type[1]['name']
        elif obj.credit_type == 3:
            return credit_type[2]['name']

    def __get_debit_type(self, obj):
        if obj.credit_type == 1:
            return debit_type[0]['name']
        elif obj.credit_type == 2:
            return debit_type[1]['name']
        elif obj.credit_type == 3:
            return debit_type[2]['name']








