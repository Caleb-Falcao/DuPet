from django.urls import path
from clinics import views

urlpatterns = [
    path('', views.clinic_list, name='clinic_list')
]
