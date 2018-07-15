from rest_framework import serializers
from transaction.models import Transaction, Budget
from home.globals import const

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


class BudgetSerializer(serializers.ModelSerializer):
    user = serializers.RelatedField

    class Meta:
        model = Budget
        fields = ('user',
                 'amount',
                 'budget_type',
                 'created_at',
                 'updated_at')

    def validate_budget_type(self, value):
        """
            check if budget_type is valid
        :param value:
        :return value:
        """
        budget_type = const.budget_type
        for b_type in budget_type:
            if value in b_type:
                return value
        raise serializers.ValidationError("Invalid Type")