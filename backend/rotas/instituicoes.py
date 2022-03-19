from django.urls import path

from quiz_app.views import instituicao

urlpatterns = [
    path("instituicoes/", instituicao.consulta_instituicao, name="instituicoes"),
    path("instituicoes/cadastro/", instituicao.cadastro_instituicao, name="cadastro_instituicao"),
    path("instituicoes/editar/<id>", instituicao.atualizar_instituicao, name="atualizar_instituicao"),
    path("instituicoes/remover/<id>", instituicao.remover_instituicao, name="remover_instituicao"),
]