from django.urls import path

from .views import SaleDetailView, SaleListView, SaleCreateView

urlpatterns = [
    path('create/', SaleCreateView.as_view(), name='sale-create'),
    path('list/', SaleListView.as_view(), name='sale-list'),
    path('detail/<int:pk>/', SaleDetailView.as_view(), name='sale-detail'),
]
