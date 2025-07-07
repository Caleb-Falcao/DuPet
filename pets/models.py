from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    ESPECIE_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('passaro', 'Pássaro'),
        ('roedor', 'Roedor'),
        ('outro', 'Outro'),        
    ]

    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=20, choices=ESPECIE_CHOICES)
    raca = models.CharField(max_length=100, blank=True)
    data_nascimento = models.DateField(null=True,blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    foto = models.ImageField(upload_to='pets_fotos/',null=True, blank=True)
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} ({self.especie})'
    
    """
    | Campo             | Função                                        |
    | ----------------- | --------------------------------------------- |
    | `dono`            | Relaciona o pet a um usuário                  |
    | `nome`            | Nome do pet                                   |
    | `especie`         | Cachorro, gato, etc. (com escolhas limitadas) |
    | `raca`            | Raça do animal (opcional)                     |
    | `data_nascimento` | Data de nascimento (opcional)                 |
    | `peso`            | Peso em kg (até 999.99)                       |
    | `foto`            | Upload de imagem (opcional)                   |
    | `observacoes`     | Campo livre para anotações                    |
    | `criado_em`       | Data de criação automática                    |
    """