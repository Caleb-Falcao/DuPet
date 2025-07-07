from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('pet_list') #redireciona para a lista de pets
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'users/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1!= password2:
            messages.error(request, 'As senhas não coincidem.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Este nome de usuário já existe.')
        else:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect('pet_list')
        
    return render(request, 'users/signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')