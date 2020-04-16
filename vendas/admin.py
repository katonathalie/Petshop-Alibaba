from django.contrib import admin
from .models import Vendas


class VendasAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'funcionario']
    search_fields = ['id', 'date']

admin.site.register(Vendas, VendasAdmin)
