from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    
# One to Many
class CarReview(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.car.name}"
    
# Many to Many
class Showroom(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    car_varieties = models.ManyToManyField(Cars, related_name='showrooms')

    def __str__(self):
        return self.name
    
# One to One
class SafetyCertificate(models.Model):
    car = models.OneToOneField(Cars, related_name='certificate', on_delete=models.CASCADE)
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.car.name}"