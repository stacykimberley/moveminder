from django.shortcuts import render

def index(request):
    return render(request, 'booking/index.html')

def home(request):
    return render(request, 'booking/index.html')

def about(request):
    return render(request, 'booking/about.html')

def classes(request):
    return render(request, 'booking/classes.html')
