from django.db import models

# Create your models here.
class CadastrodePerguntas(models.Model):
    pergunta = models.CharField(
        verbose_name='Digite sua pergunta',
        max_length=255,
        blank=False,
        null=True
    )