from django.urls import path
# from .views import CustomUserUpdateView, CustomUserDeleteView, views



from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),

    #path('delete_user/<str:pk>/', views.deleteUser, name='delete_user'),

    #path('account', views.account, name='account'),
]
   


