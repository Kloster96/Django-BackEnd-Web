from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

class Category (models.Model):
    name =models.CharField(max_length=100, verbose_name="Nombre")
    created =models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la creacion")
    updated =models.DateTimeField(auto_now=True, verbose_name="Fecha de la edicion")


    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name= "Cotenido")
    published = models.DateTimeField(verbose_name="Fecha de publicidad", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de la edicion")


    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']

    
    def __str__(self):
        return self.title