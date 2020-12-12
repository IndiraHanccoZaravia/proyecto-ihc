from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class admin_crud(TemplateView):
	template_name ='admin_crud.html'

class estadistica(TemplateView):
	template_name ='estadistica.html'

class base(TemplateView):
	template_name ='base.html'

class registration(TemplateView):
	template_name = 'registration.html'

class login(TemplateView):
	template_name = 'login.html'

class recover(TemplateView):
	template_name = 'recover.html'

class eliminar(TemplateView):
	template_name = 'eliminar.html'

