from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pet
from .forms import PetForm

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
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'pets/pet_form.html',{'form': form})
