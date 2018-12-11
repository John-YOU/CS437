# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#django imports
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt 

#rest_framework imports
from rest_framework import viewsets, filters
from django.http import HttpResponseRedirect


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

def genres(request):
    genres = GenresTable.objects.all()
    limit = 6
    paginator = Paginator(genres, limit) # 6 records per page
    page = request.GET.get('page','1')
    result = paginator.page(page)
    return render(request, 'movies/page_partition_genres.html', {'messages' : result})

def index(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')

@csrf_exempt
def moviesInfo(request):
    movies = Movie.objects.all()
    year=None
    title=None
    if request.method=="POST":
	l=request.body.find('=')+1
	s=request.body[l:]
	if l==5:
		year=s
	else:
		title=s
		title=title.replace('+',' ')
	movie=[]
	for i in range(len(movies)):
		if year!=None and str(movies[i].year)==year:
			movie.append(movies[i])
		if title!=None and movies[i].primary_title==title:
			movie.append(movies[i])
	movies=movie
    limit = len(movies)+1
    paginator = Paginator(movies, limit)
    page = request.GET.get('page','1')
    result = paginator.page(page)
    return render(request, 'movies/page_partition.html', {'messages' : result})
