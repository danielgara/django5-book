from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cart.index'),
    path('<int:id>/add_to_cart/', views.add_to_cart, name='cart.add_to_cart'),
    path('clear_cart/', views.clear_cart, name='cart.clear_cart'),
]