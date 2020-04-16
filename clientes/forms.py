from django import forms
from .models import Pet, Cliente
from django.forms import Select, DateInput

SPECIES_CHOICES = (('', 'Espécie'), ('C', 'Cachorro'), ('G', 'Gato'), ('A', 'Ave'), ('R', 'Roedor'),
                   ('P', 'Peixe'), ('R', 'Reptil'), ('Os', 'Outros'))
GENDER_CHOICES = (('', 'Gênero'), ('F', 'Fêmea'), ('M', 'Macho'), ('I', 'Indefinido'))

class ClienteCreateForm(forms.ModelForm):
    cpf = forms.CharField(max_length=11, min_length=11)

    class Meta:
        model = Cliente
        fields = ['name', 'date_of_birth', 'cpf', 'telephone', 'rua', 'numero', 'bairro', 'cidade', 'complemento', 'cep']

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'})
        }

class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'age', 'species', 'breed', 'gender']

    def __init__(self, *args, **kwargs):
        super(PetCreateForm, self).__init__(*args, **kwargs)
        self.fields['species'].widget = Select(choices=SPECIES_CHOICES, attrs={'class': 'form-control'})
        self.fields['gender'].widget = Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'})
        self.fields['date_of_birth'].widget = DateInput(attrs={'class': 'form-control'})

    def set_owner(self, id):
        pet = super(PetCreateForm, self).save(commit=False)
        pet.owner = id
        return pet.owner





