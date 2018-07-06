from rest_framework.response import Response
from rest_framework.decorators import api_view
from transaction.serializer import TransactionSerializer
from transaction.models import Transaction

@api_view(['GET'])
def transaction(request):
    if request.method == 'GET':
        trnas_raw_data = Transaction.objects.all()
        serializer = TransactionSerializer(trnas_raw_data, many=True)
        return Response(serializer.data)
