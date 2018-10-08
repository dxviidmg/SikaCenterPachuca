from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ['nombre',]
	search_fields = ['nombre',]
#	list_editable = ['nombre',]
	prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Categoria, CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
	list_display = ['nombre',]
	search_fields = ['nombre',]
#	list_editable = ['nombre',]
	prepopulated_fields = {"slug": ("nombre",)}

admin.site.register(Producto, ProductoAdmin)