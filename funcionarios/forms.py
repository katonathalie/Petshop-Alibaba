from django import forms
from .models import User
from core.mail import send_mail_template
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        password = User.objects.make_random_password()
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.initial = {'password1': password,
                        'password2': password}

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação de senha não está correta')
        return password2


    def send_mail(self):
        subject = 'Cadastro PetShop Alibaba'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'password': self.cleaned_data['password1']
        }
        template_name = 'funcionarios/register_mail.html'
        send_mail_template(subject, template_name, context, [context['email']], settings.CONTACT_EMAIL)

        return (context['email'])


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['name', 'email', 'password1']

        widgets = {'password1': forms.HiddenInput()}


class UserFormEdit(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'name', 'email',]