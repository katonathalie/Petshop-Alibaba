from django.urls import path
from vendas import views

urlpatterns = [
    path('', views.vendas_list, name='vendas_list'),
    path('cadastrar_vendas/', views.vendas_create, name='cadastrar_vendas'),
    path('cupom_fiscal/<int:id>', views.get_pdf, name='cupom_fiscal'),
    path('relatorio_vendas/', views.relatorio_vendas, name='relatorio_vendas'),

]