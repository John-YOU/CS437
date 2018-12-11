# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#django imports
from django.shortcuts import render

#rest_framework imports
from rest_framework import viewsets, filters

#serializers import
from movies.serializers import MovieSerializer, GenresTableSerializer

#models import
from movies.models import Movie, GenresTable

# Create your views here.

class GenresTableViewSet(viewsets.ModelViewSet):
	queryset = GenresTable.objects.all()
        serializer_class = GenresTableSerializer

class MovieViewSet(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

def index(request):
    return render(request, 'home.html')
