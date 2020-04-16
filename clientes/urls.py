from django.urls import path
from clientes import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('cadastrar_cliente/', views.create_client, name='cadastrar_cliente'),
    path('client_update/<int:id>', views.client_update, name='client_update'),
    path('client_delete/<int:id>', views.client_delete, name='client_delete'),

    path('cadastrar_pet/<int:id>', views.create_pet, name='cadastrar_pet'),
    path('pet_list/<int:id>', views.pet_list, name='pet_list'),
    path('pet_update/<int:id>', views.pet_update, name='pet_update'),
    path('pet_delete/<int:id>', views.pet_delete, name='pet_delete'),
]