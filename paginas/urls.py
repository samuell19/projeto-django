from django.urls import path
from .views import PaginaInicial, SobreView

urlpatterns = [
    #path('endereço'/, MinhaView.as_view(),name='nome da url'),
    path('', PaginaInicial.as_view(), name = 'inicio'),
    path('sobre/',SobreView.as_view(), name='sobre'),

]