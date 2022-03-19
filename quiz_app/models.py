from django.db import models

# Create your models here.


class Instituicao(models.Model):
    nome_instituicao = models.CharField(
        verbose_name='Nome da Instituicao de ensino',
        max_length=125
    )
    nome_curso = models.CharField(
        verbose_name='Nome do curso',
        max_length=125,
    )

    class Meta:
        db_table = "instituicao"


class Disciplina(models.Model):
    nome_disciplina = models.CharField(
        verbose_name='Disciplina',
        max_length=50,
    )
    id_instituicao = models.ForeignKey(
        Instituicao, 
        models.DO_NOTHING, 
        db_column="id_instituicao", 
        blank=False, 
        null=False
    )

    class Meta:
        db_table = "disciplina"

class Professor(models.Model):
    nome = models.CharField(
        verbose_name='Nome Completo',
        max_length=125,
        blank=False,
        null=False
    )
    id_instituicao = models.ForeignKey(
        Instituicao, 
        models.DO_NOTHING, 
        db_column="id_instituicao", 
        blank=False, 
        null=False
    )

    class Meta:
        db_table = "professor"


class CadastrodePerguntas(models.Model):
    id_professor = models.ForeignKey(
        Professor, 
        models.DO_NOTHING, 
        db_column="id_professor", 
        blank=True, 
        null=False
    )
    id_disciplina = models.ForeignKey(
        Disciplina, 
        models.DO_NOTHING, 
        db_column="id_disciplina", 
        blank=True, 
        null=False
    )
    pergunta = models.CharField(
        verbose_name='Digite sua pergunta',
        max_length=255,
        blank=False,
        null=False
    )
    alternativas = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )
    
    resposta_alternativa = models.CharField(
        max_length=1,
        choices=alternativas,
        default=alternativas[0][0],
        verbose_name='Resposta',
    )
    resposta_extenso = models.CharField(
        verbose_name='Digite a resposta',
        max_length=100
    )
    explicacao = models.TextField(
        verbose_name='Digite a explicação do livro/apostila da resposta',
        blank=True,
        null=True
    )
    dificuldade = (
        ('F', 'Fácil'),
        ('M', 'Médio'),
        ('D', 'Difícil'),
    )
    grau_de_dificuldade = models.CharField(
        max_length=1,
        choices=dificuldade,
        verbose_name='Grau de dificuldade'
    )

    class Meta:
        db_table = "cadastro_perguntas"