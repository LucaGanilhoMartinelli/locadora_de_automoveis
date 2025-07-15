from django.shortcuts import render, redirect, get_object_or_404
from .models import Automovel
from .forms import AutomovelForm

def lista_automoveis(request):
    automoveis = Automovel.objects.all().order_by('placa')
    return render(request, 'veiculos/lista_automoveis.html', {'automovel': automoveis})

def detalhe_automovel(request, placa):
    automovel = get_object_or_404(Automovel, pk=placa)
    return render(request, 'veiculos/detalhe_automovel.html', {'automovel': automovel})

def adicionar_automovel(request):
    if request.method == 'POST':
        form = AutomovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veiculos:lista_automoveis')
    else:
        form = AutomovelForm()
        return render(request, 'veiculos/adicionar_automovel.html', {'form': form, 'titulo_pagina': 'Adicionar Veículo'})