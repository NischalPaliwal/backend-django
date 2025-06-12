from django.shortcuts import render
from django.http import JsonResponse
from .models import Cars

def home(request):
    return render(request, 'app/index.html')

def show_cars(request):
    cars = Cars.objects.all()
    cars_list = []
    for car in cars:
        cars_list.append({
            'name': car.name,
            'launch_date': car.date_added,
            'type': car.type
        })
    return JsonResponse({'cars': cars_list})