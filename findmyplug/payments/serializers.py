from rest_framework import serializers
from .models import Order,Payment

class OrderDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Order
        fields= '__all__'
        
class PaymentDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
