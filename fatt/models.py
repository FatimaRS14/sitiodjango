from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
#Aqui es donde se crean las tablas para la creación de base de datos 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #IMAGE

    def __str__(self):
        return f'Perfil de {self.user.username}'
        #Esta funcion sirve para que se pueda poner el nombre sel usuario al que pertenece el perfil 


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    #se pondra la funcion default=timezone.now para que se agrege la hora y fecha cuando se cree el post
    content = models.TextField()


    class Meta:
      ordering = ['-timestamp']#esto sirve para ir ordenando los post de manera ascendente   

    def __str__(self):
        return f'{self.user.username}: {self.content}'