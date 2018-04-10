from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from django.contrib.auth.models import User
from home.serializer import UserSerializer


def home(request):
    return render(request, 'registration/login.html')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
