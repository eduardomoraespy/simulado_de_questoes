from django.shortcuts import render


def cadastro_professor(request):
    return render(request, 'index.html')

def atualizar_professor(request, id):
    return render(request, 'index.html')

def remover_professor(request, id):
    return render(request, 'index.html')