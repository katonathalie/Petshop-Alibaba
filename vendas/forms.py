from django import forms
from .models import Vendas
from django.forms import formset_factory
from itens.models import Item
from django.core.validators import MinValueValidator
from itens.forms import MONTHS
from django.utils.timezone import now



class VendasForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['date', 'funcionario', 'cliente', 'forma_pagamento']

        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.SelectDateWidget(months=MONTHS, empty_label='Cliente',
                attrs={'data-max': now, 'class': 'form-control', 'style': 'width: 33.333%; display: inline-block; margin-bottom: 6px;'}),
            'forma_pagamento': forms.Select(attrs={'class': 'form-control'}),
            'funcionario': forms.Select(attrs={'class': 'form-control'})
        }


    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date > now():
            raise forms.ValidationError('Não é possível cadastrar venda com data maior do que a atual.')
        return date



class AddItemForm(forms.Form):

    item = forms.ModelChoiceField(queryset=Item.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    quantidade = forms.IntegerField(validators=[MinValueValidator(1)], required=True,
                                    widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'margin-left: 15px;'}))

    def clean_quantidade(self):
        qntd = self.cleaned_data['quantidade']
        idItem = self['item'].value()

        if idItem != '':
            item = Item.objects.get(pk=idItem)

            if item.category == 'P':
                if item.quantity < qntd:
                    raise forms.ValidationError('Quantidade de %s indiponível.' % item.name)
                else:
                    item.baixaEstoqueProduto(qntd)
                    item.save()
        else:
            raise forms.ValidationError('Informações incorretas. Verifique os campos.')

        return qntd


ItemFormSet = formset_factory(AddItemForm, extra=1)


class PeriodoRelatorioVendas(forms.Form):

    data_inicial = forms.DateField(widget=forms.SelectDateWidget(months=MONTHS,
        attrs={'class': 'form-control', 'style': 'width: 33.333%; display: inline-block;'}))
    data_final = forms.DateField(widget=forms.SelectDateWidget(months=MONTHS,
        attrs={'class': 'form-control', 'style': 'width: 33.333%; display: inline-block;'}))

