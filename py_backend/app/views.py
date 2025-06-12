from django.shortcuts import render
from .models import Cars

def home(request):
    return render(request, 'app/index.html')

def show_cars(request):
    cars = Cars.objects.all()
    return render(cars)