from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import RegisterForm, UserFormEdit
from .models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
@staff_member_required(login_url='/')
def list_funcionario(request):
    template_name = 'funcionarios/lista.html'
    storaged = messages.get_messages(request)
    users = User.objects.all()

    context = {'users': users, 'messages': storaged}
    return render(request, template_name, context)


@login_required(login_url='/')
@staff_member_required(login_url='/')
def create_funcionario(request):
    template_name = 'funcionarios/cadastrar_funcionario.html'
    context = {}

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            context['email'] = form.send_mail()
            form.save()
            context['success'] = True
            form = RegisterForm()
    else:
        form = RegisterForm()

    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/')
def edit_password(request):
    template_name = 'funcionarios/edit_password.html'
    context = {}

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)

    context['form'] = form

    return render(request, template_name, context)


@login_required(login_url='/')
def update_funcionario(request, id):
    template_name = 'funcionarios/update_funcionario.html'
    funcionario = get_object_or_404(User, pk=id)
    context = {}

    form = UserFormEdit(request.POST or None, instance=funcionario)

    if request.method == 'POST':
        form = UserFormEdit(request.POST, instance=funcionario)

        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário atualizado com sucesso!')

            return redirect('lista')

    context['form'] = form
    context['user'] = funcionario

    return render(request, template_name, context)


@staff_member_required(login_url='/')
def deactivate_funcionario(request, id):
    funcionario = get_object_or_404(User, pk=id)

    if request.method == 'GET':
        funcionario.is_active = False
        funcionario.save(force_update=True)
        messages.success(request, 'O funcionário agora está inativo no sistema!')

    return redirect('lista')


@staff_member_required(login_url='/')
def reactivate_funcionario(request, id):
    funcionario = get_object_or_404(User, pk=id)

    if request.method == 'GET':
        funcionario.is_active = True
        funcionario.save(force_update=True)
        messages.success(request, 'O funcionário agora está ativo no sistema!')

    return redirect('lista')

