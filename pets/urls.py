from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path("<int:pet_id>/", views.pet_detail, name="pet_detail"),
    path('novo/', views.pet_create, name='pet_create'),
    path('<int:pk>/editar/', views.pet_edit, name='pet_edit'),
    path('<int:pk>/excluir', views.pet_delete, name='pet_delete'),    
    path('<int:pet_id>/vacina/add/', views.adicionar_vacina, name='adicionar_vacina'),
    path('<int:pet_id>/alimentacao/add/', views.adicionar_alimentacao, name='adicionar_alimentacao'),
    path('<int:pet_id>/consulta/add/', views.adicionar_consulta, name='adicionar_consulta'),
    path('<int:pet_id>/peso/add/',views.adicionar_peso, name='adicionar_peso'),
]
