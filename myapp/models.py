from django.db import models

class Obra(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    dimensiones = models.CharField(max_length=100)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_artista = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

    