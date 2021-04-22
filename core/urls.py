from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'core'

urlpatterns = [
    path('susmap/all/', views.list_all_susmap),
    path('card/user/', views.list_user),
    path('login/', views.login_user),
    path('card/detail/<id>/', views.card_detail),
    path('card/forms/', views.forms),
    path('card/forms/submit', views.set_cardform),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('', RedirectView.as_view(url="susmap/all/")),
    path('unidades/listar', views.unidades_listar, name='unidades-listar'),
    path('atendimento/finalizar', views.finalizar_atendimento, name='finalizar-atendimento'),
    path('atendimento/listar', views.fila_atendimento, name='fila-atendimento'),
    path('servico/cadastrar/', views.fila_atendimento, name='servico-cadastrar')
]