from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    #Modelo para almacenar los posts

    autor =  models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length= 200)
    text = models.TextField()

    fechaCreacion = models.DateField(
        default = timezone.now
    )
    fechaPublicacion = models.DateField(
        blank= True, null=True
    )
    def publicar(self):
        """
        Método para obetener la fecha de publicacion cuando se publique algún post
        """
        self.fechaPublicacion=timezone.now()
        self.save()

#método magico que nos permite castear un objeto a una cadena
    def __str__(self):
        return self.titulo