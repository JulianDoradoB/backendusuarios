from django.db import models

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  
    nombre = models.CharField(max_length=100)
    fotoPerfil = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    banner = models.ImageField(upload_to='banners/', blank=True, null=True)
    experiencia = models.TextField(blank=True, null=True)
    educacion = models.TextField(blank=True, null=True)
    habilidades = models.TextField(blank=True, null=True)
    certificaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
