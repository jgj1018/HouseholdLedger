from .models import  Budget

# Create your views here.
from .serializer import BudgetSerializer
from rest_framework import viewsets
from home.globals import functions
from django_filters import rest_framework as filters
from .filter import BudgetFilter
from home.views import AuthenticateView

class BudgetViewSet(viewsets.ModelViewSet, AuthenticateView):
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



