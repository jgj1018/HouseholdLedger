from .models import  Budget

# Create your views here.
from .serializer import BudgetSerializer
from rest_framework import viewsets


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer