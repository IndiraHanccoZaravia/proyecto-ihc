from django.urls import path
from main.views import *
from . import views

urlpatterns = [
	path("admin_crud", admin_crud.as_view(),name="admin_crud"),
	path("registration", registration.as_view(), name = "registration"),
	path("login", login.as_view(), name = "login"),
	path("recover", recover.as_view(), name = "recover"),
	path("eliminar", eliminar.as_view(), name = "eliminar"),
	path("base", base.as_view(), name = "base"),
]