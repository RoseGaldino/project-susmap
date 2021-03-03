from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    city = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    beging_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class card:
        db_table = 'card'

#Usuário
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=10)

#Paciente
#numeroSUS, Ranking
class Paciente(models.Model):
    numeroSUS = models.CharField(max_length=10)

class Atendente(models.Model):
    unidadeAtendimento = models.CharField(max_length=20)

class Administrador(models.Model):
    gerenciamentoAtendentes = models.CharField(max_length=20)