from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=200 ,verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    content = models.TextField(verbose_name= "Contenido")
    image = models.ImageField(verbose_name= "Imagenes", upload_to= "services")
    created =models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la creacion")
    updated =models.DateTimeField(auto_now=True, verbose_name="Fecha de la edicion")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    
    def __str__(self):
        return self.title
        