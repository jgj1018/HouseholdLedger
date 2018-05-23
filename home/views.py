from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from django.contrib.auth.models import User
from home.serializer import UserSerializer
from django.http import HttpResponse, JsonResponse
from custom_serializer.CodeSerializer import CodeSerializer
from rest_framework import serializers
from home.globals import const


def home(request):
    return render(request, 'base.html')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


def transaction_types(request):
    transaction_type = const.transaction_type
    return JsonResponse(transaction_type, safe=False)
