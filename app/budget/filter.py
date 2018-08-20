from django_filters import rest_framework as filters
from .models import Budget
class BudgetFilter(filters.FilterSet):
    updated_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Budget
        fields = ['updated_at']