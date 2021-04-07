from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Card

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

def form_sintomas(request, id):
    sintomas =  Sintomas.objects.get(active=True, id=id)
    print(sintomas.id)
    return render(request, 'model-formulario.html', {'sintomas':sintomas})

@login_required(login_url='/login/')
def forms(request):
    return render(request, 'model-formulario.html')

@login_required(login_url='/login/')
def set_cardform(request):
    return redirect('/')

@login_required(login_url='/login/')
def register_unidades(request):
    return render(request, 'register_unid.html')

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
