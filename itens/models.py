from django.db import models


class ItemManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(code__icontains=query)
        )

class Item(models.Model):

    name = models.CharField('Nome do item', max_length=100, unique=True)
    code = models.CharField('Codigo', max_length=8, unique=True, null=False)
    created_at = models.DateField('Cadastrado em', auto_now_add=True)
    quantity = models.IntegerField('Quantidade', blank=True, default=0)
    description = models.TextField('Descriçao do item', blank=True)
    price_of_sale = models.DecimalField('Preço de venda', max_digits=8, decimal_places=2, blank=False, default=0, null=False)
    price_of_buy = models.DecimalField('Preço de compra', max_digits=8, decimal_places=2, blank=True, default=0, null=False)
    expiration_date = models.DateField('Data de validade', blank=True, null=True)
    category = models.CharField('Categoria', max_length=8, blank=False, null=False, choices=(('S', 'Serviço'), ('P', 'Produto')))

    objects = ItemManager()

    def __str__(self):
        return self.name

    def baixaEstoqueProduto(self, quantidade):
        if self.category == 'P':
            self.quantity = self.quantity - quantidade
            return self.quantity

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering = ['name']