from django.contrib import admin
from .models import Cars
from .models import CarReview
from .models import Showroom
from .models import SafetyCertificate

admin.site.register(Cars, CarReview, Showroom, SafetyCertificate)