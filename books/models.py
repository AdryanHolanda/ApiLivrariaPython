from django.db import models
from uuid import uuid4
# Create your models here.


class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    estado = models.CharField(max_length=50)
    total_de_paginas = models.IntegerField()
    editora = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)