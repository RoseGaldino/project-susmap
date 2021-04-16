from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Card, Sintoma, Qualificador, UnidadeSaude, Servico

# Create your views here.
@login_required(login_url='/login/')
def list_all_susmap(request):
    card = Card.objects.filter(active=True)
    return render(request, 'list.html', {'card':card})
#Dicionário -> {'card':card}, 'card' vai ser todo resultado de Card.objects.filter(active=True)

def list_user(request):
    card = Card.objects.filter(active=True, user=request.user)
    return render(request, 'list.html', {'card': card})

def card_detail(request, id):
    card = Card.objects.get(active=True, id=id)
    print(card.id)
    return render(request, 'card.html', {'card':card})

@login_required(login_url='/login/')
def forms(request):
    sintoma =  Sintoma.objects.all()
    context = {'sintoma': sintoma}
    return render(request, 'model-formulario.html', context)

@login_required(login_url='/login/')
def set_cardform(request):
    return redirect('/')

@login_required(login_url='/login/')
def register_unidades(request):
    return render(request, 'register_unid.html')
    
@login_required(login_url='/login/')
def unidades_listar(request):
    sintomas_all = Sintoma.objects.all()
    sintomas_sets = []
    for s in sintomas_all:
        sintomas = request.POST[s.nome]
        if len(sintomas):
            sintomas_sets.append(s)
    print(sintomas_sets)

    ## Identificando os serviços relacionados aos sintomas
    servicos_set = []
    for servico in Servico.objects.all():
        for sintoma in servico.sintoma.all():
            if sintoma in sintomas_sets:
                print('Serviço --> ' + servico.nomeServico)
                servicos_set.append(servico)

    ## Identificando as unidades relacionadas aos serviços
    unidades_set = []
    for unidade in UnidadeSaude.objects.all():
        for servico in unidade.servico.all():
            if servico in servicos_set:
                print('Unidade --> ' + unidade.nomeUnidadeSaude)
                unidades_set.append(unidade)
    
    return render(request, 'unidades-listar.html', { 'unidades': unidades_set })

@login_required(login_url='/login/')
def set_card(request):
    city = request.POST.get('city')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    description = request.POST.get('description')
    photo = request.FILES.get('file')
    user = request.user
    card = Card.objects.create(email=email, phone=phone, description=description,
                                photo=photo, user=user)
    print(city)
    return redirect('/')

def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username)
        #print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Senha ou Usuário inválido')
    return redirect('/login/')
