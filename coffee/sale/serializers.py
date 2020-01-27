from rest_framework import serializers

from .models import Sale


class SaleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = (
            'id',
            'user_name',
            'drink_name',
            'price',
            'quantity',
            'price_total',
        )


class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
