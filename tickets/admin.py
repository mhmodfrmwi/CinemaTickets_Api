from django.contrib import admin

# Register your models here.
from .models import Guest,Reservation,Movie

admin.site.register(Guest)
admin.site.register(Movie)
admin.site.register(Reservation)