from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from django.contrib.auth.models import User
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from home.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from home.globals import const


def home(request):
    return render(request, 'base.html')


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


