from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100,unique=True, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False)