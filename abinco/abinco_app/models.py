from django.db import models

class ClaseBase(models.Model):
    creado_el = models.DateField(auto_now_add=True)
    actualizado_el = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True

class Categoria(ClaseBase):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Marca(ClaseBase):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Ubicacion(ClaseBase):
    zona = models.CharField(max_length=100)

    def __str__(self):
        return self.zona


class Producto(ClaseBase):
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo




