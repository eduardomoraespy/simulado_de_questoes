from django.shortcuts import render


def cadastro_disciplina(request):
    return render(request, 'index.html')

def atualizar_disciplina(request, id):
    return render(request, 'index.html')

def remover_disciplina(request, id):
    return render(request, 'index.html')