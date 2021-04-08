from django.contrib import admin
from .models import Card
from .models import Qualificadores
from .models import Sintomas
from .models import Servico
from .models import UnidadeSaude

# Register your models here.
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'description', 'user']

@admin.register(Qualificadores)
class QualificadoresAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Sintomas)
class SintomasAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomeServico']

@admin.register(UnidadeSaude)
class UnidadeSaudeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nomeUnidadeSaude']

