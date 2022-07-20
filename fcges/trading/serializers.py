from rest_framework import serializers

from trading.models import OrderBlock


class OrderBlockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderBlock
        fields = '__all__'
