from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/create/', views.create_review, name='movies.create_review'),
    path('<int:id>/delete/<int:review_id>/', views.delete_review, name='movies.delete_review'),
]