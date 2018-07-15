from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from django.contrib.auth.models import User
from home.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.globals import const


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
        get TransactionTypeData
    """
    if request.method == 'GET':
        transaction_type = const.transaction_type
        return Response(transaction_type)


@api_view(['GET'])
def budget_types(request):
    """
    get:
        get BudgetTypeData
    """
    if request.method == 'GET':
        budget_type = const.budget_type

        return Response(budget_type)

