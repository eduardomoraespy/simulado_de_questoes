from django.shortcuts import render


def cadastro_pergunta(request):
    return render(request, 'index.html')

def atualizar_pergunta(request, id):
    return render(request, 'index.html')

def remover_pergunta(request, id):
    return render(request, 'index.html')