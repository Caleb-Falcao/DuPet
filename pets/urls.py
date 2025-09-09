from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path("<int:pet_id>/", views.pet_detail, name="pet_detail"),
    path('novo/', views.pet_create, name='pet_create'),
    path('<int:pk>/editar/', views.pet_edit, name='pet_edit'),
    path('<int:pk>/excluir', views.pet_delete, name='pet_delete'),    
]
