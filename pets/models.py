from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F','Fêmea'),
    ]
    
    PORTE_CHOICES = [
        ('P','Pequeno'),
        ('M','Médio'),
        ('G','Grande')
    ]
    
    ESPECIE_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('passaro', 'Ave'),
        ('roedor', 'Roedor'),
        ('outro', 'Outro'),        
    ]

    
    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, default='M')
    cor = models.CharField(max_length=50, blank=True, null=True)
    porte = models.CharField(max_length=1, choices=PORTE_CHOICES, blank=True, null=True)
    microchip = models.CharField(max_length=50, blank=True, null=True, unique=True)
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=20, choices=ESPECIE_CHOICES)
    raca = models.CharField(max_length=100, blank=True)
    data_nascimento = models.DateField(null=True,blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    foto = models.ImageField(upload_to='pets/',null=True, blank=True)
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
    
class Vacina(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='vacinas')
    nome = models.CharField(max_length=100) # Ex.: Antirrabica
    data_aplicacao = models.DateField()
    proxima_dose = models.DateField(blank=True, null=True)
    veterinario = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nome} - {self.pet.nome}"
    
class Alimentacao(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="alimentacoes")
    descricao = models.CharField(max_length=100, default="Ração")
    quantidade = models.CharField(max_length=50, blank=True, null=True)
    horario = models.TimeField()
    
    def __str__(self):
        return f"{self.pet.nome} - {self.descricao} às {self.horario}"
    

class Consulta(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='consultas')
    data = models.DateTimeField()
    local = models.CharField(max_length=100, blank=True, null= True)
    veterinario = models.CharField(max_length=100, blank=True, null=True)
    motivo = models.CharField(max_length=200)
    observacoes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Consulta {self.pet.nome} - {self.data.strftime('%d/%m/%Y')}"

class Peso(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='pesos')
    data = models.DateField(auto_now_add=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.pet.nome} - {self.peso} kg em {self.data}"