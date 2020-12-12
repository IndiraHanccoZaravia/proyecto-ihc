from django.urls import path
from main.views import *
from . import views

urlpatterns = [
	path("grafico", grafico.as_view(), name = "grafico"),
	path("admin_crud", admin_crud.as_view(),name="admin_crud"),
	path("registration", registration.as_view(), name = "registration"),
	path("login", login.as_view(), name = "login"),
	path("recover", recover.as_view(), name = "recover"),
	path("eliminar", eliminar.as_view(), name = "eliminar"),
	path("estadistica", estadistica.as_view(), name = "estadistica"),
	path("", base.as_view(), name = "base"),
]