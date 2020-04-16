from django.db import models
from funcionarios.models import User
from clientes.models import Cliente
from itens.models import Item


class ItemCompradoManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(item__icontains=query)
        )

class ItemComprado(models.Model):
    item = models.ForeignKey(Item, verbose_name='Item', on_delete=models.CASCADE)
    qnt = models.IntegerField(default=1, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2)

    objects = ItemCompradoManager()


class VendasManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(code__icontains=query) |
            models.Q(date__icontains=query) |
            models.Q(cliente__icontains=query)
        )

class Vendas(models.Model):

    date = models.DateTimeField('Data da venda')
    funcionario = models.ForeignKey(User, verbose_name='Funcionário', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.CASCADE)
    itens = models.ManyToManyField(ItemComprado, blank=True)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    forma_pagamento = models.CharField('Forma de Pagamento', max_length=20, choices=(
        ('D', 'Dinheiro'), ('CC', 'Cartão de Crédito'), ('CD', 'Cartão de Débito')), default=('D', 'Dinheiro'))

    objects = VendasManager()

    def __str__(self):
        return 'Código: %d - Cliente: %s ' % (self.pk, self.cliente)


    def calculaValor_total(self):
        valor_total = 0
        for itemComprado in self.itens.all():
            valor_total += itemComprado.subtotal
        self.valor_total = valor_total

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'



