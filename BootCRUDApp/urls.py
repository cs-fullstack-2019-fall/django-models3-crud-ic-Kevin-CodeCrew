from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('display/<int:pk>/', views.display, name='display'),
    path('index/', views.index, name="index"),
    path('login/', views.logIn, name="logIn"),
    path('logout/', views.logOut, name="logout"),
    path('newUser', views.newUser, name="newUser"),
    path('', views.list, name='list'),
]
