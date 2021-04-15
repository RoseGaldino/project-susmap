from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Card(models.Model):
    city = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    beging_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='card')
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class card:
        db_table = 'card'


class Qualificador(models.Model):
    nome = models.CharField(max_length=50)
    sintoma = models.ForeignKey("Sintoma", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class card:
        db_table = 'qualificador'

class Sintoma(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return str(self.id)

    def __eq__(self, sintoma):
        if (isinstance(sintoma, Sintoma)):
            return self.nome == sintoma.nome
        return False

    class card:
        db_table = 'sintoma'

#Usuário
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=10)

#Paciente
class Paciente(models.Model):
    numeroSUS = models.CharField(max_length=10)
    ranking = models.CharField(max_length=300)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )

class Atendente(models.Model):
    unidadeAtendimento = models.CharField(max_length=20)

class Administrador(models.Model):
    gerenciamentoAtendentes = models.CharField(max_length=20)

class Atendimento(models.Model):
    filaEspera = models.CharField(max_length=200)
    sintoma = models.ManyToManyField(Sintoma)

class Endereco(models.Model):
    rua = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.rua

class Servico(models.Model):
    nomeServico = models.CharField(max_length=100)
    descricaoServico = models.CharField(max_length=100)
    sintoma = models.ManyToManyField(Sintoma)

class UnidadeSaude(models.Model):
    nomeUnidadeSaude = models.CharField(max_length=50)
    enderecoUnidade = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
    servico = models.ManyToManyField(Servico)

class Localizacao(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()

