# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.generics import CreateAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponse

from .models import *
from .serializers import *
from .forms import *
from rest_framework.permissions import(
    IsAuthenticated,
    IsAdminUser,
    AllowAny,
)

class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    permission_classes =  [AllowAny,]
    serializer_class = MovieSerializer
    

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
            movies = Movie.objects.all()
            context = {
                'movies': movies,
            }
        return render(request, 'home.html', context)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'add_movie.html', context)

def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'home.html', context)

def movie_detail(request, pk):
    print(pk)
    movie = Movie.objects.get(id = pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movie_detail.html',context)