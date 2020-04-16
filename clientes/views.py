from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Pet
from django.contrib import messages
from .forms import PetCreateForm, ClienteCreateForm
from django.contrib.auth.decorators import login_required

# ------------- CLIENTE -------------- #

@login_required(login_url='/')
def create_client(request):
    template_name = 'clientes/cadastrar_cliente.html'
    storaged = messages.get_messages(request)
    cliente = None

    if(request.method == 'POST'):
        form = ClienteCreateForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            messages.success(request, 'Cliente incluído com sucesso.')
            return redirect('client_update', id=cliente.id)
    else:
        form = ClienteCreateForm()

    context = {
        'form': form,
        'message': storaged,
    }
    return render(request, template_name, context)


@login_required(login_url='/')
def client_list(request):
    clients = Cliente.objects.all()
    template_name = 'clientes/client_list.html'
    return render(request, template_name, {'clients': clients})


@login_required(login_url='/')
def client_update(request, id):
    client = get_object_or_404(Cliente, pk=id)
    storaged = messages.get_messages(request)
    form = ClienteCreateForm(request.POST or None, instance=client)
    template_name = 'clientes/client_update.html'
    context = {'client': client, 'form': form, 'message': storaged}

    if form.is_valid():
        form.save()
        context['success'] = True

    return render(request, template_name, context)


@login_required(login_url='/')
def client_delete(request, id):
    client = get_object_or_404(Cliente, pk=id)

    client.delete()
    messages.success(request, 'Cliente excluído com sucesso.')

    return redirect('client_list')



# --------------- PET ---------------- #


@login_required(login_url='/')
def create_pet(request, id):
    owner = get_object_or_404(Cliente, pk=id)
    template_name = 'clientes/cadastrar_pet.html'
    context = {}

    if request.method == 'POST':
        form = PetCreateForm(request.POST)
        form.set_owner(owner)
        if form.is_valid():
            form.save()
            context['success'] = True
            form = PetCreateForm()
    else:
        form = PetCreateForm()

    context['form'] = form
    context['owner'] = owner
    return render(request, template_name, context)


@login_required(login_url='/')
def pet_list(request, id):
    owner = get_object_or_404(Cliente, pk=id)
    pets = Pet.objects.filter(owner=owner)
    storaged = messages.get_messages(request)
    template_name = 'clientes/pet_list.html'
    return render(request, template_name, {'pets': pets, 'owner': owner, 'message': storaged})


@login_required(login_url='/')
def pet_update(request, id):
    pet = get_object_or_404(Pet, pk=id)
    owner = get_object_or_404(Cliente, pk=pet.owner.id)
    template_name = 'clientes/pet_update.html'
    form = PetCreateForm(request.POST or None, instance=pet)

    if form.is_valid():
        form.save()
        messages.success(request, 'Dados atualizados com sucesso.')
        return redirect('pet_list', id=owner.pk)

    context = {'form': form, 'pet': pet, 'owner': owner}

    return render(request, template_name, context)


@login_required(login_url='/')
def pet_delete(request, id):
    pet = get_object_or_404(Pet, pk=id)
    owner = get_object_or_404(Cliente, pk=pet.owner.id)

    pet.delete()
    messages.success(request, 'Animal excluído com sucesso.')

    return redirect('pet_list', id=owner.pk)
