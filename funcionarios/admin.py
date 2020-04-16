from django.contrib import admin
from .forms import RegisterForm
from .models import User


class UserChangeForm(RegisterForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'is_staff',]
        exclude = ['password1', 'password2']


class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm

    list_display = ['name', 'email', 'is_staff']

admin.site.register(User, UserAdmin)
