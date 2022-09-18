from rest_framework import viewsets

from core.models import Stock, StockInfo
from core.serializers import StockSerializer, StockInfoSerializer
# Create your views here.
class StockViewset(viewsets.ModelViewSet):
    """
    Stock viewset
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockInfoViewset(viewsets.ModelViewSet):
    """
    StockInfo viewset
    """
    queryset = StockInfo.objects.all()
    serializer_class = StockInfoSerializer