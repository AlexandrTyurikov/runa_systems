from rest_framework import serializers

from .models import Drink


class DrinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('id', 'name', 'price')


class DrinkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = '__all__'
