from django.urls import path
from . import views

app_name = 'veiculos'

urlpatterns = [
    path('', views.lista_automoveis , name='lista_automoveis'),
    path('<int:pk>/', views.detalhe_automovel, name='detalhe_automovel'),
    path('novo/', views.adicionar_automovel, name='adicionar_automovel'),
]