from django.shortcuts import render, get_object_or_404, redirect
from .models import Vendas, ItemComprado
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from .forms import VendasForm, ItemFormSet, PeriodoRelatorioVendas
from django.contrib import messages
from core.render import Render
from decimal import Decimal
from django.db.models import Sum
from django.contrib.admin.views.decorators import staff_member_required


@login_required(login_url='/')
def vendas_list(request):
    template_name = 'vendas/vendas_list.html'
    context = {}
    storaged = messages.get_messages(request)

    vendas = Vendas.objects.all()

    context['vendas'] = vendas
    context['messages'] = storaged

    return render(request, template_name, context)


@login_required(login_url='/')
def get_pdf(request, id):
    venda = get_object_or_404(Vendas, pk=id)
    tributo = Decimal(float(venda.valor_total) * 0.2215).quantize(Decimal('.01'))

    params = {
        'venda': venda,
        'tributo': tributo
    }
    return Render.render('vendas/cupom_fiscal.html', params)


@login_required(login_url='/')
def vendas_create(request):
    template_name = 'vendas/cadastrar_vendas.html'
    context = {}

    if request.method == 'GET':
        vendaForm = VendasForm(request.GET or None,
               initial={'funcionario': request.user, 'date': now})
        formset = ItemFormSet(request.GET or None)

    elif request.method == 'POST':
        vendaForm = VendasForm(request.POST, initial={'funcionario': request.user, 'date': now})
        formset = ItemFormSet(request.POST)

        if vendaForm.is_valid() and formset.is_valid():
            venda = vendaForm.save()
            context['venda'] = venda

            for form in formset:
                itemComprado = ItemComprado.objects.create(
                    item=form.cleaned_data.get('item'),
                    qnt=form.cleaned_data.get('quantidade'),
                    subtotal=form.cleaned_data.get('quantidade')*form.cleaned_data.get('item').price_of_sale
                )
                itemComprado.save()

                if itemComprado:
                    venda.itens.add(itemComprado)
                venda.calculaValor_total()
                venda.save()

            if venda.itens.exists():
                context['success'] = True
            else:
                venda.delete()
                messages.error(request, 'Venda sem itens não cadastrada.')
                return redirect('vendas_list')


    context['vendaForm'] = vendaForm
    context['formset'] = formset

    return render(request, template_name, context)


# def get(context):
#     return Render.render('vendas/relatorio_vendas_pdf.html', context)


@staff_member_required(login_url='/')
def relatorio_vendas(request):
    template_name = 'vendas/relatorio_vendas.html'
    form = PeriodoRelatorioVendas(initial={'data_inicial': now, 'data_final': now})
    context = {}
    total_vendido = Decimal(0).quantize(Decimal('.01'))

    if request.method == 'POST':
        form = PeriodoRelatorioVendas(request.POST, initial={'data_inicial': now, 'data_final': now})
        if form.is_valid():
            data_inicial = form.cleaned_data['data_inicial']
            data_final = form.cleaned_data['data_final']

            vendas = Vendas.objects.filter(date__range=[data_inicial, data_final]).order_by('date')
            if vendas:
                total_vendido = Decimal(vendas.aggregate(total=Sum('valor_total'))['total']).quantize(Decimal('.01'))

            context = {
                'vendas': vendas,
                'data_inicial': data_inicial,
                'data_final': data_final,
                'total_vendido': total_vendido
            }

            return Render.render('vendas/relatorio_vendas_pdf.html', context)

    context['form'] = form

    return render(request, template_name, context)



