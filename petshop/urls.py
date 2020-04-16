"""petshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import urls as core_urls
from clientes import urls as clientes_urls
from funcionarios import urls as funcionarios_urls
from itens import urls as produtos_servicos_urls
from vendas import urls as vendas_urls
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('clientes/', include(clientes_urls), name='clientes'),
    path('funcionarios/', include(funcionarios_urls), name='funcionarios'),
    path('produtos_servicos/', include(produtos_servicos_urls), name='produtos_servicos'),
    path('vendas/', include(vendas_urls), name='vendas'),
]


handler404 = 'core.views.handle_page_not_found'


