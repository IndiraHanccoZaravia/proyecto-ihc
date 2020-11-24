from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class registration(TemplateView):
	template_name = 'registration.html'

class login(TemplateView):
	template_name = 'login.html'

class recover(TemplateView):
	template_name = 'recover.html'