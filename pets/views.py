from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pet
from .forms import PetForm

@login_required
def pet_list(request):
    # Lista apenas os pets do dono logado
    pets = Pet.objects.filter(dono=request.user)
    return render(request, 'pets/pet_list.html', {'pets': pets})


@login_required
def pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.dono = request.user  # associa automaticamente ao dono logado
            pet.save()
            return redirect('pets:pet_list')
    else:
        form = PetForm()
    return render(request, 'pets/pet_form.html', {'form': form})


@login_required
def pet_edit(request, pk):
    # Garante que só o dono pode editar
    pet = get_object_or_404(Pet, pk=pk, dono=request.user)

    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets:pet_list')
    else:
        form = PetForm(instance=pet)

    return render(request, 'pets/pet_form.html', {'form': form, 'pet': pet})


@login_required
def pet_delete(request, pk):
    # Garante que só o dono pode excluir
    pet = get_object_or_404(Pet, pk=pk, dono=request.user)
    if request.method == 'POST':
        pet.delete()
        return redirect('pets:pet_list')
    return render(request, 'pets/pet_confirm_delete.html', {'pet': pet})

def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, dono=request.user)
    return render(request, "pets/pet_detail.html", {"pet":pet})