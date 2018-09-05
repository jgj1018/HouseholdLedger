from django_filters import rest_framework as filters
from .models import Transaction


class TransactionFilter(filters.FilterSet):
    updated_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Transaction
        fields = ['updated_at']