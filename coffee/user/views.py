from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import UserDetailSerializer
from .models import User


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (IsAdminUser,)


class UserListView(generics.ListAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)
