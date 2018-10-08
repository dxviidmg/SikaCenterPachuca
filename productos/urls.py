from django.urls import path
from .views import *

app_name = "productos"

urlpatterns = [
	path('lista/', ProductoList.as_view(), name="producto-list"),
]