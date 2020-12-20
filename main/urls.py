from django.urls import path
from main.views import *
from . import views

urlpatterns = [
	path("grafico1", grafico1.as_view(), name = "grafico1"),
	path("grafico2", grafico2.as_view(), name = "grafico2"),
	path("grafico3", grafico3.as_view(), name = "grafico3"),
	path("grafico4", grafico4.as_view(), name = "grafico4"),
	path("grafico5", grafico5.as_view(), name = "grafico5"),

	path("mapa",  mapaSitio.as_view(), name = "mapa"),	

	path("admin_crud", admin_crud.as_view(),name="admin_crud"),
	path("registration", registration.as_view(), name = "registration"),
	path("login", login.as_view(), name = "login"),
	path("recover", recover.as_view(), name = "recover"),
	path("eliminar", eliminar.as_view(), name = "eliminar"),	
	path("", base.as_view(), name = "base"),
]