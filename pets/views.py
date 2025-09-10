from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pet, Vacina
from .forms import PetForm, VacinaForm, AlimentacaoForm, ConsultaForm, PesoForm

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

#Vacina Form, AlimetacaoForm, ConsultaForm, PesoForm

def adicionar_vacina(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == "POST":
        form = VacinaForm(request.POST)
        if form.is_valid():
            vacina = form.save(commit=False)
            vacina.pet = pet
            vacina.save()
            return redirect("pets:pet_detail", pet.id)
    
    else:
        form = VacinaForm()
    
    return render(request, "pets/adicionar_vacina.html", {"form": form, "pet": pet})


def adicionar_alimentacao(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == "POST":
        form = AlimentacaoForm(request.POST)
        if form.is_valid():
            alimentacao = form.save(commit=False)
            alimentacao.pet = pet
            alimentacao.save()
            return redirect("pets:pet_detail", pet.id)
    
    else:
        form = AlimentacaoForm()
    
    return render(request, "pets/adicionar_alimentacao.html", {"form": form, "pet": pet})


def adicionar_consulta(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == "POST":
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.pet = pet
            consulta.save()
            return redirect("pets:pet_detail", pet.id)
    
    else:
        form = ConsultaForm()
    
    return render(request, "pets/adicionar_consulta.html", {"form": form, "pet": pet})

def adicionar_peso(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == "POST":
        form = PesoForm(request.POST)
        if form.is_valid():
            peso = form.save(commit=False)
            peso.pet = pet
            peso.save()
            return redirect("pets:pet_detail", pet.id)
    
    else:
        form = PesoForm()
    
    return render(request, "pets/adicionar_peso.html", {"form": form, "pet": pet})