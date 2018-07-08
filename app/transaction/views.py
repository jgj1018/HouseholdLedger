from django.shortcuts import render
from rest_framework.decorators import api_view

from .models import Transaction

# Create your views here.
from .serializer import TransactionSerializer
from rest_framework import viewsets


# @api_view(['GET'])
# def transaction(request):
#     if request.method == 'GET':
#         trnas_raw_data = Transaction.objects.all()
#         serializer = TransactionSerializer(trnas_raw_data, many=True)
#         return Response(serializer.data)
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer