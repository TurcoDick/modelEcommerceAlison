
from django.db import models

# Create your models here.
# Esses modelos são classes que representam tabelas da nossa aplicação catalogo

class Category(models.Model):

    # CharField = varchar em BD
    name = models.CharField('nome',max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    # salva a data e hora de criação da tabela
    created = models.DateTimeField('criado em',auto_now_add=True)

    # salva a data e hora do ultimo salve feito
    modified = models.DateTimeField('Modificado em',auto_now=True)


class Meta:
    verbose_name ='Categoria'
    verbose_name_plural = 'Categorias'

    # ordenar os nomes em ordem crescente
    ordering = ['name']

    # ordenar os nomes em ordem decrescente
    # ordering = ['-name']