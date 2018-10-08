from django.shortcuts import render
from .models import *
from django.views.generic import View
#from carrito.forms import CartAddProductForm

class ProductoList(View):
	def get(self, request, slug=None):
		template_name= "productos/producto_list.html"

		if slug:
			categoria = Categoria.objects.get(slug=slug)
			productos = Producto.objects.all().filter(categoria=categoria)
		else:
			productos = Producto.objects.all()

		categorias = Categoria.objects.all()
		print(categorias)
#		form = CartAddProductForm()
		context = {
		'productos': productos,
		'categorias': categorias,
		
#		'form':  form,
		}
		return render(request, template_name, context)