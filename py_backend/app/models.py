from django.db import models
from django.utils import timezone

class Cars(models.Model):
    car_type_choice = [('HTB', 'Hatchback'),
                       ('SD', 'Sedan'),
                       ('SUV', 'SUV'), 
                       ('MUV', 'MUV'), 
                       ('LX', 'Luxury')]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=car_type_choice)

    def __str__(self):
        return self.name