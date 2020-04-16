from django.db import models

class ClienteManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(cpf__icontains=query)
        )

class Cliente(models.Model):
    name = models.CharField('Nome completo', max_length=100, blank=False)
    cpf = models.CharField('CPF', max_length=15, blank=False, unique=True, null=False)
    telephone = models.CharField('Telefone', max_length=12, blank=False, null=True)
    rua = models.CharField('Rua', max_length=200, blank=True, null=True)
    cep = models.CharField('CEP', max_length=9, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=30, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=20, blank=True, null=True)
    numero = models.CharField('Número', max_length=5, blank=True, null=True)
    complemento = models.CharField('Complemento', max_length=20, blank=True, null=True)
    date_of_birth = models.DateField('Data de nascimento', blank=True, null=True)

    objects = ClienteManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('client_update', args=[str(self.id)])




class PetManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(owner__icontains=query)
        )

class Pet(models.Model):

    owner = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=50, blank=True, null=True)
    date_of_birth = models.DateField('Data de Nascimento', blank=True, null=True)
    age = models.IntegerField('Idade', blank=True, null=True)
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    species = models.CharField('Espécie', max_length=20, choices=(
        ('C', 'Cachorro'), ('G', 'Gato'), ('A', 'Ave'), ('R', 'Roedor'), ('P', 'Peixe'), ('R', 'Reptil'), ('Os', 'Outros')),
                               blank=False, null=True)
    breed = models.CharField('Raça', max_length=30, null=True, blank=True)
    gender = models.CharField('Gênero', max_length=8, choices=(('F', 'Fêmea'), ('M', 'Macho'), ('I', 'Indefinido')))

    objects = PetManager()

    def __str__(self):
        return self.name + '(' + self.owner.name + ')'


    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering = ['owner', 'name']

