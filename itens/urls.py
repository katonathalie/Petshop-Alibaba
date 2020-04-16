from django.urls import path
from itens import views

urlpatterns = [
    path('cadastrar_produto/', views.produto_create, name='produto_create'),
    path('listar_produtos/', views.produto_list, name='produto_list'),
    path('editar_produto/<int:id>', views.produto_update, name='produto_update'),
    path('apagar_produto/<int:id>', views.produto_delete, name='produto_delete'),

    path('relatorio_estoque/', views.get, name='relatorio_estoque'),

    path('cadastrar_servico/', views.servico_create, name='servico_create'),
    path('listar_servicos/', views.servico_list, name='servico_list'),
    path('editar_servico/<int:id>', views.servico_update, name='servico_update'),
    path('apagar_servico/<int:id>', views.servico_delete, name='servico_delete'),
]