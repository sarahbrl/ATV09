from django.shortcuts import render, get_object_or_404
from .models import Conteudo, Menu

def home(request):
    # Obtém o menu dinâmico e o primeiro conteúdo ativo para a home
    menu_itens = Menu.objects.filter(ativo=True)
    conteudo_principal = Conteudo.objects.filter(ativo=True).first()

    context = {
        'menu_itens': menu_itens,
        'conteudo': conteudo_principal
    }
    return render(request, 'base.html', context)

def detalhe_conteudo(request, slug):
    # Obtém o menu dinâmico e o conteúdo correspondente ao slug
    menu_itens = Menu.objects.filter(ativo=True)
    conteudo = get_object_or_404(Conteudo, slug=slug, ativo=True)

    context = {
        'menu_itens': menu_itens,
        'conteudo': conteudo
    }
    return render(request, 'conteudo.html', context)
