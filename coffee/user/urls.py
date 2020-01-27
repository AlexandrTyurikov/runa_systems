from django.urls import path

from .views import UserCreateView, UserDetailView, UserListView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('list/', UserListView.as_view(), name='user-list'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
