from django.db import models
from django.conf import settings

# Create your models here.

class Users(models.Model):
    usuario = models.CharField(max_length=16)
    senha = models.CharField(max_length=16)
    email = models.CharField(max_length=256)

class Upload(models.Model):
    id_upload = models.AutoField(primary_key=True, editable=False)
    img = models.ImageField(upload_to='images/', blank=False, null=False)
    nome = models.CharField(max_length=255)
    user = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nome

class Mockup(models.Model):
    id_mockup = models.AutoField(primary_key=True, editable=False)
    imagem = models.ForeignKey(Upload, on_delete=models.CASCADE, null=False)
    cor = models.CharField(max_length=255, null=False)
    vermelho = models.CharField(max_length=255, null=True)
    verde = models.CharField(max_length=255, null=True)
    azul = models.CharField(max_length=255, null=True)
    user = models.IntegerField(blank=True, null=True)


