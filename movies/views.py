# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#django imports
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt 

#rest_framework imports
from rest_framework import viewsets, filters

#serializers import
from movies.serializers import MovieSerializer, GenresTableSerializer

#models import
from movies.models import Movie, GenresTable, Rating
from decimal import Decimal

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
    return render(request, 'movies/page_partition_movies.html', {'messages' : result})

class movie_rating(object):
    def __init__(self,primary_title,year,runtime,average_rating,number_of_votes):
        self.primary_title=primary_title
        self.year=year
        self.runtime=runtime
        self.average_rating=average_rating
        self.number_of_votes=number_of_votes

@csrf_exempt
def rating(request):
    l=request.body.find('=')+1
    s=request.body[l:]
    r=Decimal(s.strip(' "'))
    movie = Movie.objects.all()
    dict={}
    for i in range(len(movie)):
	dict[movie[i].movie_id]=(movie[i].primary_title,movie[i].year,movie[i].runtime)
    ratings = Rating.objects.all()
    movies=[]
    for i in range(len(ratings)):
        if ratings[i].average_rating>=r:
            id=ratings[i].movie_id
            rating=ratings[i].average_rating
            votes=ratings[i].number_of_votes
            movies.append(movie_rating(dict[id][0],dict[id][1],dict[id][2],rating,votes))
    limit = len(movies)+1
    movies.sort(key=lambda x:x.average_rating,reverse=True)
    paginator = Paginator(movies, limit)
    page = request.GET.get('page','1')
    result = paginator.page(page)
    return render(request, 'movies/page_partition_ratings.html', {'messages' : result})

@csrf_exempt
def popularity(request):
    l=request.body.find('=')+1
    s=request.body[l:]
    n=int(s)
    movie = Movie.objects.all()
    dict={}
    for i in range(len(movie)):
        dict[movie[i].movie_id]=(movie[i].primary_title,movie[i].year,movie[i].runtime)
    ratings = Rating.objects.all()
    movies=[]
    for i in range(len(ratings)):
        id=ratings[i].movie_id
        rating=ratings[i].average_rating
        votes=ratings[i].number_of_votes
        movies.append(movie_rating(dict[id][0],dict[id][1],dict[id][2],rating,votes))
    limit = len(movies)+1
    movies.sort(key=lambda x:x.number_of_votes,reverse=True)
    movie=movies
    movies=[]
    for i in range(n):
        movies.append(movie[i])
    paginator = Paginator(movies, limit)
    page = request.GET.get('page','1')
    result = paginator.page(page)
    return render(request, 'movies/page_partition_ratings.html', {'messages' : result})
