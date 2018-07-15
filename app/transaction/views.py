from .models import Transaction, Budget

# Create your views here.
from .serializer import TransactionSerializer, BudgetSerializer
from rest_framework import viewsets


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer