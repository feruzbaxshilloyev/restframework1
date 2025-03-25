from django.urls import path
from .views import CreateView, UpdateDestroyView, DeleteView, home

urlpatterns = [
    path('', home, name='home'),
    path('create/', CreateView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateDestroyView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteView.as_view, name='delete'),
]
