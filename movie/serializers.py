from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class MovieSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields= '__all__'