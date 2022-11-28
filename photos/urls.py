from django.urls import path
from . import views

urlpatterns = [
    path('', views.photos, name='photos'),
    path('photo/<int:pk>/', views.viewPhoto, name='photo'),
    path('edit/<int:pk>/', views.updatePhoto, name='edit'),
    path('delete/<int:pk>/', views.deletePhoto, name='delete'),
    path('add/', views.addPhoto, name='add'),
]