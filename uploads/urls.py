from django.urls import path
from . import views
from uploads.views import DeletePhotoView
urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    path('delete_photo/<pk>/', DeletePhotoView, name='delete_photo'),

]
