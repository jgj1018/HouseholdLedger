from .models import Transaction

# Create your views here.
from .serializer import TransactionSerializer
from rest_framework import viewsets


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
