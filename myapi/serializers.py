# serializers.py
from rest_framework import serializers

from .models import Hero, Sidekicks

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name', 'alias')

class SideKicksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sidekicks
        fields = ('id','name', 'alias')