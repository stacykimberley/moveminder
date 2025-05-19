from django.shortcuts import render
from .models import GymClass

def index(request):
    return render(request, 'booking/index.html')

def home(request):
    return render(request, 'booking/index.html')

def about(request):
    return render(request, 'booking/about.html')

def classes(request):
    classes = GymClass.objects.all()
    return render(request, 'booking/classes.html', {'classes': classes})
