from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pet
from .forms import PetForm

@login_required
def pet_edit(request, pk):
    # Pega o pet, garante que é do usuário logado
    pet = get_object_or_404(Pet, pk=pk, dono=request.user)

    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets:pet_list')
    else:
        form = PetForm(instance=pet)

    # Sempre retorna o render, mesmo se for GET ou POST inválido
    return render(request, 'pets/pet_form.html', {'form': form, 'pet': pet})

#descomentar depois
#@login_required
#lista de pets
def pet_list(request):
    #mostrar apenas pets do dono
    pets = Pet.objects.filter(dono=request.user)
    return render(request, 'pets/pet_list.html', {'pets':pets})

#criar pets
@login_required
def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.dono = request.user
            pet.save()
            return redirect('pets:pet_list')
    else:
        form = PetForm()
    return render(request, 'pets/pet_form.html',{'form': form})

@login_required
def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk, dono=request.user)
    if request.method == 'POST':
        pet.delete()
        return redirect('pets:pet_list')
    return render(request, 'pets/pet_confirm_delete.html', {'pet': pet})