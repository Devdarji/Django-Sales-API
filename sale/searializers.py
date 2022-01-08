from django.db.models import fields
from rest_framework import serializers
from .models import Sale

class SaleSerializer(serializers.ModelSerializer):
    itemType_name = serializers.CharField(source='itemType.name')
    class Meta:
        model = Sale
        fields = ['id','order_id', 'region', 'country',
                  'itemType_name', 'sales_channel', 'order_priority', 'order_date', 'ship_date', 'unit_sold', 'unit_price', 'unit_cost']
        
