from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='noticias_imagenes/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    contenido = models.TextField()

    def __str__(self):
        return self.nombre
