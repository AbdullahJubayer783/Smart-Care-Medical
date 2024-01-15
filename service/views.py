from django.shortcuts import render
from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializers
# Create your views here.
class ServieceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers