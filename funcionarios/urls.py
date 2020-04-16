from django.urls import path, include
from funcionarios import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='funcionarios/login.html'), name='login'),
    path('edit_password/', views.edit_password, name='edit_password'),
    path('', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view, name='password_reset'),

    path('cadastrar_funcionario/', views.create_funcionario, name='cadastrar_funcionario'),
    path('lista/', views.list_funcionario, name='lista'),
    path('editar_funcionario/<int:id>', views.update_funcionario, name='editar_funcionario'),
    path('desativar_funcionario/<int:id>', views.deactivate_funcionario, name='desativar_funcionario'),
    path('reativar_funcionario/<int:id>', views.reactivate_funcionario, name='reativar_funcionario'),
]