import re
from rest_framework.response import Response
from rest_framework import status,serializers
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer,RefreshJSONWebTokenSerializer
from django.contrib.auth.models import User


class JwtExpiCheck():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        response = None
        try:
            if self._is_passible(path):
                response = self.get_response(request)
            elif self._check_jwt(request):
                token = self._get_token(request)
                refreshed = RefreshJSONWebTokenSerializer().validate(attrs={'token': token})
                response = self.get_response(request)
                response.data['token'] = refreshed['token']
                response.status = status.HTTP_200_OK
        except Exception as e:
            response = Response(status=status.HTTP_403_FORBIDDEN)
        finally:
            return response

    def _is_passible(self, path):
        is_account = bool(re.match('^/account/.+', path))
        is_favicon = bool(re.match('^/favicon.ico/$', path))
        is_home = bool(re.match('^/home/$', path))
        is_transaction = bool(re.match('^/transaction/$', path))
        is_index = bool(re.match('^/$', path))
        is_swagger = bool(re.match('^/swagger/$', path))

        if is_account or is_favicon or is_home or is_index or is_swagger or is_transaction:
            return True
        else:
            return False

    def _check_jwt(self, request):
        token = self._get_token(request)
        data = {'token': token}
        try:
            valid_data = VerifyJSONWebTokenSerializer().validate(data)
        except serializers.ValidationError as e:
            raise serializers.ValidationError
        user = valid_data['user']
        return isinstance(user, User)

    def _get_token(self, request):
        if request.method == 'GET':
            params = request.GET
        else:
            params = request.POST
        token = params['token']
        return token
