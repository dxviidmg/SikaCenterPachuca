from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
	path('', Home.as_view(), name="home"),
	path('contacto/', Nosotros.as_view(), name="nosotros"),
]