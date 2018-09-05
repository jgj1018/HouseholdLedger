from .models import  Budget

# Create your views here.
from .serializer import BudgetSerializer
from rest_framework import viewsets
from home.globals import functions
from django_filters import rest_framework as filters
from .filter import BudgetFilter


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    lookup_field = 'user'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BudgetFilter

    def get_queryset(self):
        user = self.request.query_params['user']
        queryset = functions.filter_by_user_id(Budget.objects, {'user': user})
        return queryset


