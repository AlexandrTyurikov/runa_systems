from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import SaleDetailSerializer, SaleListSerializer
from .models import Sale


class SaleCreateView(generics.CreateAPIView):
    serializer_class = SaleDetailSerializer


class SaleListView(generics.ListAPIView):
    serializer_class = SaleListSerializer
    queryset = Sale.objects.all()
    permission_classes = (IsAdminUser, )


class SaleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SaleDetailSerializer
    queryset = Sale.objects.all()
    permission_classes = (IsAdminUser,)
