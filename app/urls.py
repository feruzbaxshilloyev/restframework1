from django.urls import path
from .views import CreateView, UpdateDestroyView

urlpatterns = [
    path('create/', CreateView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateDestroyView.as_view(), name='update'),
]
