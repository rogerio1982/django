from django.db import models

# Create your models here.
class Todo(models.Model):
    task =models.CharField(max_length=30)
    description =models.CharField(max_length=100)

class Clientes(models.Model):
    nome =models.CharField(max_length=30)
    desdescricao =models.CharField(max_length=100)