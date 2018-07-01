"""HouseholdLedger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(url='http:/0.0.0.0:8000/')

from home import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^account/', include('rest_auth.urls'), name='account'),

    url(r'^account/registration/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/', refresh_jwt_token),
    url(r'^home/$',views.home, name='home'),
    url(r'^transaction/$',views.transaction, name='transaction'),
    url(r'^boot/$',views.transaction_types, name='boot'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^swagger/$', schema_view)

]


