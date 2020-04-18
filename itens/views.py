from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm, ServicoForm
from django.utils import timezone
from core.render import Render

@login_required(login_url='/')
def get(request):
    produtos = Item.objects.filter(category='P')
    today = timezone.now()
    params = {
        'today': today,
        'produtos': produtos,
    }
    return Render.render('produtos/relatorio_estoque_pdf.html', params)

# --------------------------------------------------------------------- PRODUTOS

@login_required(login_url='/')
def produto_list(request):
    produtos = Item.objects.filter(category='P')
    template_name = 'produtos/produto_list.html'

    return render(request, template_name, {'produtos': produtos})


@login_required(login_url='/')
def produto_create(request):
    template_name = 'produtos/produto_create.html'
    context = {}

    if (request.method == 'GET'):
        form = ProdutoForm(request.GET or None)
    elif(request.method == 'POST'):
        form = ProdutoForm(request.POST, initial={'category': 'Produto'})

        if form.is_valid():
            form.save()
            form = ProdutoForm()
            context['success'] = True
    # else:
    #     form = ProdutoForm(request.GET or None)

    context['form'] = form

    return render(request, template_name, context)


@login_required(login_url='/')
def produto_update(request, id):
    template_name = 'produtos/produto_update.html'
    produto = get_object_or_404(Item, pk=id)
    context = {}

    form = ProdutoForm(request.POST or None, instance=produto)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')

            return redirect('produto_list')

    context['form'] = form

    return render(request, template_name, context)


@login_required(login_url='/')
def produto_delete(request, id):
    produto = get_object_or_404(Item, pk=id)

    produto.delete()
    messages.success(request, 'Produto excluído com sucesso!')

    return redirect('produto_list')



# --------------------------------------------------------------------- SERVIÇOS

@login_required(login_url='/')
def servico_list(request):
    servicos = Item.objects.filter(category='S')
    template_name = 'servicos/servico_list.html'
    storaged = messages.get_messages(request)

    return render(request, template_name, {'servicos': servicos, 'messsages': storaged})


@login_required(login_url='/')
def servico_create(request):
    template_name = 'servicos/servico_create.html'
    context = {}

    if(request.method == 'POST'):
        form = ServicoForm(request.POST)

        if form.is_valid():
            form.save()
            form = ServicoForm()
            context['success'] = True

    else:
        form = ServicoForm()

    context['form'] = form

    return render(request, template_name, context)


@login_required(login_url='/')
def servico_update(request, id):
    template_name = 'servicos/servico_update.html'
    servico = get_object_or_404(Item, pk=id)
    context = {}

    form = ServicoForm(request.POST or None, instance=servico)

    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)

        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço atualizado com sucesso!')

            return redirect('servico_list')

    context['form'] = form

    return render(request, template_name, context)


@login_required(login_url='/')
def servico_delete(request, id):
    servico = get_object_or_404(Item, pk=id)

    servico.delete()
    messages.success(request, 'Serviço excluído com sucesso!')

    return redirect('servico_list')
