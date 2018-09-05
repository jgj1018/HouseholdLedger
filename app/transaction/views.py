from .models import Transaction
from home.globals import functions
from .serializer import TransactionSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .filter import TransactionFilter


# Create your views here.
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TransactionFilter

    def get_queryset(self):
        user = self.request.query_params['user']
        queryset = functions.filter_by_user_id(Transaction.objects, {'user': user})
        return queryset

