from django.db import models

# Create your models here.
# Guest Movie Reservation
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    duration = models.IntegerField()
    rating = models.FloatField()
    hall=models.CharField(max_length=10)
    seats_available=models.IntegerField()

# Guest

class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

# Movie Reservation

class Reservation(models.Model):
    guest = models.ForeignKey(Guest,related_name='reservation', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,related_name='reservation', on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()