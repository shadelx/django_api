from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer, SideKicksSerializer
from .models import Hero, Sidekicks


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class SideKicksViewSet(viewsets.ModelViewSet):
    queryset = Sidekicks.objects.all().order_by('name')
    serializer_class = SideKicksSerializer