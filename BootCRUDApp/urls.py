from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('list/', views.list, name='list'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('display/<int:pk>/', views.display, name='display'),
    path('', views.index, name=''),
]
