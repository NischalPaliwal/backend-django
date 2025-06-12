from django.shortcuts import render
from django.http import JsonResponse
from .models import Cars

def home(request):
    return render(request, 'app/index.html')

def show_cars(request):
    cars = Cars.objects.all()
    return JsonResponse(cars)