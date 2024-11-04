from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from .views import PerfilView



urlpatterns=[
    #path('endereço'/, MinhaView.as_view(),name='nome da url'),
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'
        ),name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', PerfilView.as_view(), name='perfil'),


]