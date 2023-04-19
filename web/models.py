from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.
class pistolas(models.Model):
    nombre = models.CharField(max_length=40)
    fps = models.IntegerField()

    def __str__(self):
        return f"Pistola {self.nombre}, FPS: {self.fps}"


class aSalto(models.Model):
    nombre = models.CharField(max_length=30)
    fps = models.IntegerField()
    tipo = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='asaltos', blank=True, null=True)

    def __str__(self):
        return f"Arma de asalto {self.nombre}, FPS: {self.fps}, Tipo: {self.tipo}"


class dMr(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    fps = models.IntegerField()

    def __str__(self):
        return f"DMR {self.nombre}, Tipo: {self.tipo}, FPS: {self.fps}"
