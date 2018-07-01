from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from django.contrib.auth.models import User
from home.serializer import UserSerializer
from home.serializer import TransactionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.globals import const
from home.models import Transaction


def home(request):
    return render(request, 'base.html')


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@api_view(['GET'])
def transaction_types(request):
    """
    get:
    API endpoint that allows users to be viewed or edited.
    """
    if request.method == 'GET':
        transaction_type = const.transaction_type
        return Response(transaction_type)

@api_view(['GET'])
def transaction(request):
    if request.method == 'GET':
        trnas_raw_data = Transaction.objects.all()
        serializer = TransactionSerializer(trnas_raw_data, many=True)
        return Response(serializer.data)
