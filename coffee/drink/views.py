from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import DrinkDetailSerializer, DrinkListSerializer
from .models import Drink


class DrinkCreateView(generics.CreateAPIView):
    serializer_class = DrinkDetailSerializer
    permission_classes = (IsAdminUser,)


class DrinkListView(generics.ListAPIView):
    serializer_class = DrinkListSerializer
    queryset = Drink.objects.all()
    permission_classeses = (IsAdminUser, IsAuthenticated)


class DrinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DrinkDetailSerializer
    queryset = Drink.objects.all()
    permission_classes = (IsAdminUser,)
