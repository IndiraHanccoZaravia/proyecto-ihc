from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class admin_crud(TemplateView):
	template_name ='admin_crud.html'

class grafico1(TemplateView):
	template_name ='grafico1.html'

class grafico2(TemplateView):
	template_name = 'grafico2.html'

class grafico3(TemplateView):
	template_name = 'grafico3.html'

class grafico4(TemplateView):
	template_name = 'grafico4.html'

class grafico5(TemplateView):
	template_name = 'grafico5.html'

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

class mapaSitio(TemplateView):
	template_name = 'mapa.html'