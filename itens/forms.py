from django import forms
from .models import Item

MONTHS = {
    1:('01'), 2:('02'), 3:('03'), 4:('04'),
    5:('05'), 6:('06'), 7:('07'), 8:('08'),
    9:('09'), 10:('10'), 11:('11'), 12:('12')
}

class ServicoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ServicoForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [('S', 'Serviço')]

    class Meta:
        model = Item
        fields = ['category', 'code', 'name', 'description', 'price_of_sale']

        widgets = {
            'price_of_sale': forms.NumberInput(attrs={'class': 'form-control'})
        }



class ProdutoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [('P', 'Produto')]


    class Meta:
        model = Item
        fields = ['category', 'code', 'name', 'description', 'quantity', 'price_of_buy', 'price_of_sale', 'expiration_date']

        widgets = {
            'expiration_date': forms.SelectDateWidget(months=MONTHS, attrs={'class': 'form-control',
                                                            'style': 'width: 33.333%; '
                                                            'display: inline-block; '
                                                            'margin-bottom: 6px;'}),
            'price_of_buy': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_of_sale': forms.NumberInput(attrs={'class': 'form-control'})
        }


