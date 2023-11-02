from django.contrib import admin
from .models import Reserva, Stand

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display=('stand','nome_empresa','cnpj','data_cadastro','quitado',)

@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display=('localizacao','valor',)

# Register your models here.
