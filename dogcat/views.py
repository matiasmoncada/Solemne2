from django.shortcuts import render
from .models import Persona

# Create your views here.

def index(request):
	return render(request, 'dogcat/index.html', {})