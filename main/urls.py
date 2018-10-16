from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
	path('', Home.as_view(), name="home"),
	path('nosotros/', Nosotros.as_view(), name="nosotros"),
	path('contacto/', Contacto.as_view(), name="contacto"),	
]