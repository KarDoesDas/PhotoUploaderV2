from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('delete_photo/<str:pk>/', views.deletePhoto, name='delete_photo'),
    path('delete_folder/<str:pk>/', views.deleteFolder, name='delete_folder'),
]
