from django.shortcuts import render
from .models import Persona

# Create your views here.

def index(request):
	return render(request, 'dogcat/index.html', {})

def nostros(request):
	return render(request, 'dogcat/nosotros.html', {})

def servicios(request):
	return render(request, 'dogcat/servicios.html', {})

def contacto(request):
	return render(request, 'dogcat/contacto.html', {})