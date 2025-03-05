from django.shortcuts import render
from django.http.response import JsonResponse

from tickets.serializers import GuestSerializer,MovieSerializer,ReservationSerializer
from .models import Guest,Reservation,Movie

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import Http404
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

# rest from model

@api_view(['GET', 'POST'])
def fbv(request):
    if request.method=="GET":
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def fbv_detail(request,pk):
    if request.method =="GET":
        guest=Guest.objects.get(pk=pk)
        serializer=GuestSerializer(guest)
        return Response(serializer.data,status.HTTP_200_OK)
    elif request.method =="PUT":
        guest=Guest.objects.get(pk=pk)
        serializer=GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =="DELETE":
        guest=Guest.objects.get(pk=pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#CBV class based views
class CBV_List(APIView):
    def get(self,request):
        guests=Guest.objects.all()
        serializer=GuestSerializer(guests,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class CBV_pk(APIView):
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        guest=self.get_object(pk)
        serializer=GuestSerializer(guest)
        return Response(serializer.data)
    
    def put(self,request,pk):
        guest=self.get_object(pk)
        serializer=GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        guest=self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# mixins list

from rest_framework import mixins
from rest_framework.generics import GenericAPIView

class Mixin_List(mixins.ListModelMixin,mixins.CreateModelMixin, GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class Mixin_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)

# generic views

from rest_framework import generics

class Generic_List(generics.ListCreateAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

class Generic_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

# viewsets

from rest_framework import viewsets

class GuestViewSet(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

class ModelViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer