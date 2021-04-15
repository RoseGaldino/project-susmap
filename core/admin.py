from django.contrib import admin
from .models import Card
from .models import Qualificador
from .models import Sintoma
from .models import Servico
from .models import UnidadeSaude
from .models import Paciente
from .models import Endereco

# Register your models here.
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'description', 'user']

@admin.register(Qualificador)
class QualificadoresAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']

@admin.register(Sintoma)
class SintomasAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomeServico']

@admin.register(UnidadeSaude)
class UnidadeSaudeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomeUnidadeSaude']

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['numeroSUS', 'ranking', 'user']

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'pais']

