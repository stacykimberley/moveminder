from django.shortcuts import render

def index(request):
    return render(request, 'booking/index.html')


def home(request):
    return render(request, 'booking/index.html')