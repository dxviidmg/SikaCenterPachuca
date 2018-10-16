from django.shortcuts import render
from .models import *
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ProductoList(View):
	def get(self, request, slug=None):
		template_name= "productos/producto_list.html"

		if slug:
			categoria = Categoria.objects.get(slug=slug)
			productos_list = Producto.objects.all().filter(categoria=categoria).order_by('?')
		else:
			productos_list = Producto.objects.all()

		categorias = Categoria.objects.all()

		paginator = Paginator(productos_list, 32)
		page = request.GET.get('page')
		try:
			productos = paginator.page(page)
		except PageNotAnInteger:
			productos = paginator.page(1)
		except EmptyPage:
			productos = paginator.page(paginator.num_pages)

		context = {
		'productos': productos,
		'categorias': categorias,
		
#		'form':  form,
		}
		return render(request, template_name, context)


