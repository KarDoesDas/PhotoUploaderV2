from django.urls import path
# from .views import CustomUserUpdateView, CustomUserDeleteView, views



from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),

    # path('<int:pk>/update/', CustomUserUpdateView.as_view(template_name='accounts/update.html'), name='account_update'),
    # path('<int:pk>/delete/', CustomUserDeleteView.as_view(template_name='accounts/delete.html'), name='account_delete'),
]
   


