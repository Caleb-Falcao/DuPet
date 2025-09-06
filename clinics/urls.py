from django.urls import path
from clinics import views

app_name = 'clinics'

urlpatterns = [
    path('', views.clinic_list, name='clinic_list'),
    path("nova/", views.clinic_add, name="clinic_add"),
    path('proximas/', views.clinics_nearby, name='clinics_nearby'),
]
