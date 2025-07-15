from django.urls import path
from . import views

app_name = 'veiculos'

urlpatterns = [
    path('/veiculos/', views.lista_automoveis , name='lista_automoveis'),
    path('/veiculos/<placa_do_veiculo>/', views.detalhe_automovel, name='detalhe_automovel'),
    path('/veiculos/novo/', views.adicionar_automovel, name='adicionar_automovel'),
]