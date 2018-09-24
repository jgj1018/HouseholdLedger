from .models import Transaction
from home.globals import functions
from .serializer import TransactionSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .filter import TransactionFilter
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from home.globals import const
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TransactionFilter

    def get_queryset(self):
        user = self.request.user.id
        queryset = functions.filter_by_params(Transaction.objects, {'user': user})
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        transaction = get_object_or_404(Transaction, user= self.request.user.id, transaction_id= kwargs['pk'])
        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication, ))
def transaction_types(request):
    """
    get:
        get TransactionTypeData
    """
    if request.method == 'GET':
        transaction_type = const.transaction_type
        return Response(transaction_type)
