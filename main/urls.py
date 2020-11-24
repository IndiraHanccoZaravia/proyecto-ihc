from django.urls import path
from main.views import *
from . import views

urlpatterns = [
	path("registration", registration.as_view(), name = "registration"),
	path("login", login.as_view(), name = "login"),
	path("recover", recover.as_view(), name = "recover"),
]