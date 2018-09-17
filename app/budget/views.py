from .models import  Budget

# Create your views here.
from .serializer import BudgetSerializer
from rest_framework import viewsets
from home.globals import functions
from django_filters import rest_framework as filters
from .filter import BudgetFilter
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from home.globals import const
from rest_framework.response import Response


class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    lookup_field = 'user'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BudgetFilter

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user.id
        queryset = functions.filter_by_user_id(Budget.objects, {'user': user})
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['GET'])
@authentication_classes((JSONWebTokenAuthentication, ))
def budget_types(request):
    """
    get:
        get BudgetTypeData
    """
    if request.method == 'GET':
        budget_type = const.budget_type

        return Response(budget_type)

