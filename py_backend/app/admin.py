from django.contrib import admin
from .models import Cars
from .models import CarReview
from .models import Showroom
from .models import SafetyCertificate

admin.site.register(Cars)
admin.site.register(CarReview)
admin.site.register(Showroom)
admin.site.register(SafetyCertificate)