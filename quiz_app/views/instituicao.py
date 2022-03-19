from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
#from ..serializers import *

from ..forms import instituicao
from ..models import *

def consulta_instituicao(request):
    query_instituicao = Instituicao.objects.all()
    
    return render(
        request,
        'instituicoes/instituicao_consulta.html',
        {
            'instituicoes': query_instituicao
        }
    )

def cadastro_instituicao(request):
    form = instituicao.CadastroInstituicaoForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        form = instituicao.CadastroInstituicaoForm()

        messages.success(
            request, f'Cadastrado com sucesso'
        )

        if request.POST.get("continuar_cadastro", False):
            return redirect('cadastro_instituicao')
        else:
            return redirect('instituicoes')
    else:
        messages.error(request, form.errors)

    return render(
        request,
        'instituicoes/instituicao_form.html',
        {
            'form': form
        }
    )
    

def atualizar_instituicao(request, id):
    return render(request, 'index.html')

def remover_instituicao(request, id):
    return render(request, 'index.html')