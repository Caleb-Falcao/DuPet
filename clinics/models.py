from django.db import models

class Clinic(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True,null=True)
    
    def __str__(self):
        return self.nome
