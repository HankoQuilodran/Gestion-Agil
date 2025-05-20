from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.CharField(max_length=100) 
    stock = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"
    
    def imagen_url(self):
        return f'/media/productos/{self.imagen}'
    
    def __str__(self):
        return self.nombre
