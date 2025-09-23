from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password

def home(request):
    return render(request,'core/home.html')

@login_required
def profile(request):
    return render(request,'core/profile.html')

@login_required



@login_required
def settings(request):
    if request.method == "POST":
        user = request.user
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        altered = False

        # Se o username mudou
        if username and username != user.username:
            user.username = username
            altered = True

        # Se o email mudou
        if email and email != user.email:
            user.email = email
            altered = True

        # Se o usuário digitou nova senha
        if password:
            user.password = make_password(password)
            altered = True

        if altered:
            user.save()
            messages.success(request, "✅ Dados atualizados com sucesso!")
        else:
            messages.info(request, "Nenhuma alteração feita.")

    return render(request, "core/settings.html")


