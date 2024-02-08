from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout, name='accounts.logout'),
    path('login/', views.login, name='accounts.login'),
    path('signup/', views.signup, name='accounts.signup'),
    path('orders/', views.orders, name='accounts.orders'),
]