from django.shortcuts import render

def clinic_list(request):
    # lista ficticia de clinicas para teste
    clinics = [
        {'nome':'Clinica Animal Vida', 'endereco': 'Rua dos Bichos, 123'},
        {'nome': 'VetCuidado', 'endereco': 'Av.Pet Lovers, 456'},
        {'nome': 'Pet Saúde Total', 'endereco': 'Rua dos Animais, 789'},
    ]
    
    return render(request, 'clinics/clinic_list.html', {'clinics': clinics})

