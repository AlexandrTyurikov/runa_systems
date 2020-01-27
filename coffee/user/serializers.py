from rest_framework import serializers

from .models import User


# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username',
#             'password',
#             'last_name',
#             'is_superuser',
#             'is_staff',
#         )


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'  # Показать все поля встроенного пользователя
        fields = (
            'id',
            'username',
            'last_name',
            'password',
            'is_superuser',
            'is_staff',
        )
