from django.urls import path

from .views import DrinkCreateView, DrinkListView, DrinkDetailView

urlpatterns = [
    path('drink/create/', DrinkCreateView.as_view(), name='drink-create'),
    path('list/', DrinkListView.as_view(), name='drink-list'),
    path('drink/detail/<int:pk>/', DrinkDetailView.as_view(), name='drink-detail'),
]
