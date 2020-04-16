from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'quantity', 'created_at', 'price_of_sale', 'expiration_date']
    search_fields = ['name', 'code']

admin.site.register(Item, ItemAdmin)