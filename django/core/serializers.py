from rest_framework import serializers
from core.models import Stock, StockInfo

class StockSerializer(serializers.ModelSerializer):
    """
    Stock serializer
    """
    class Meta:
        model =  Stock
        fields = '__all__'

class StockInfoSerializer(serializers.ModelSerializer):
    """
    StockInfo serializer
    """
    class Meta:
        model =  StockInfo
        fields = '__all__'
        depth = 2