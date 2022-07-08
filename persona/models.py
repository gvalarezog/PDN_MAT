from django.db import models

# Create your models here.
class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=100)
    predeterminada = models.BooleanField(default=True)

    def __str__(self):
        return f'id: {self.id}, pais: {self.pais}, calle: {self.calle}'


class Telefono(models.Model):
    telefono = models.CharField(max_length=10)
    tipo = models.CharField(max_length=20, default='Celular')
    predeterminado = models.BooleanField(default=True)

    def __str__(self):
        return f'id: {self.id}, telefono: {self.telefono}, default: {self.predeterminado}'


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True)
    telefono = models.ForeignKey(Telefono, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'id: {self.id}, nombre: {self.apellido} {self.nombre}'
