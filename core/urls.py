from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('susmap/all/', views.list_all_susmap),
    path('card/user/', views.list_user),
    path('login/', views.login_user),
    path('card/detail/<id>/', views.card_detail),
    path('card/forms/', views.forms),
    path('card/forms/submit', views.set_cardform),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('card/register/', views.register_unidades),
    path('card/register/submit', views.set_card),
    path('', RedirectView.as_view(url="susmap/all/"))
    path('unidades/listar', views.unidades_listar, name='unidades-listar')
]