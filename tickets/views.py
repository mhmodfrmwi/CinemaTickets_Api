from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest,Reservation,Movie
# Create your views here.

# without rest and no model query

def no_rest_no_model(request):
    guests=[
        {"name": "John Doe", "age": 30},
        {"name": "Jane Smith", "age": 25},
        {"name": "Bob Johnson", "age": 35}
    ]
    return JsonResponse(guests,safe=False)

# no rest from model
def no_rest_with_model(request):
    data=Guest.objects.all()
    response={
        'guests':list(data.values('first_name','last_name','phone_number'))
    }
    return JsonResponse(response)