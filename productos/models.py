from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']

class Producto(models.Model):
	categoria = models.ForeignKey(Categoria, related_name="categoria", on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(null=True, blank=True)
	codigo = models.CharField(max_length=30)
	precio = models.DecimalField(max_digits=7, decimal_places=2)
	imagen = models.ImageField(upload_to='imagen/%Y/%m/%d/')
	ficha_tecnica = models.FileField(upload_to='ficha_tecnica/%Y/%m/%d/', null=True, blank=True)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return '{}'.format(self.nombre)

	class Meta:
		ordering = ['nombre']