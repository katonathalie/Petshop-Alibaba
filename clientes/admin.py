from django.contrib import admin
from .models import Cliente, Pet


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'date_of_birth']
    search_fields = ['name', 'cpf']


admin.site.register(Cliente, ClienteAdmin)

class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'date_of_birth', 'age']
    search_fields = ['name', 'owner']


admin.site.register(Pet, PetAdmin)

from django import forms


