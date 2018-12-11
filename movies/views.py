# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#django imports
from django.shortcuts import render
from django.core.paginator import Paginator

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

def movies(request):
    movies = Movie.objects.all()
    limit = 10
    paginator = Paginator(movies, limit) # 10 records per page
    page = request.GET.get('page','1')
    result = paginator.page(page)
    return render(request, 'movies/page_partition.html', {'messages' : result})

# show all the genres
def show_all_genres(request):
    genres = GenresTable.objects.all()
    limit = 6
    paginator = Paginator(genres, limit) # 10 records per page
    page = request.GET.get('page','1')
    result = paginator.page(page)
    return render(request, 'movies/page_partition_genres.html', {'messages' : result})

def index(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')
