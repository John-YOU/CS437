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
from movies.models import Movie, GenresTable, Rating, GenreRe
from decimal import Decimal

# Create your views here.

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
        title=s.replace('+',' ')
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
    movies.sort(key=lambda x:x.average_rating)
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

@csrf_exempt
def genreMovies(request):
    l=request.body.find('=')+1
    s=request.body[l:]
    allMovies = Movie.objects.all()
    dict={}
    for i in range(len(allMovies)):
        dict[allMovies[i].movie_id]=i
    genres = GenresTable.objects.all()
    id=None
    for i in range(len(genres)):
        if genres[i].genres_name==s:
            id=genres[i].genres_id
    movie = GenreRe.objects.all()
    movies=[]
    for i in range(len(movie)):
        if movie[i].genre_id1==id or movie[i].genre_id2==id or movie[i].genre_id3==id:
            movies.append(allMovies[dict[movie[i].movie_id]])
    movies.sort(key=lambda x:x.year)
    limit = len(movies)+1
    paginator = Paginator(movies, limit)
    page = request.GET.get('page','1')
    result = paginator.page(page)
    return render(request, 'movies/page_partition_movies.html', {'messages' : result})

@csrf_exempt
def director(request):
    movies=[]
    limit = len(movies)+1
    paginator = Paginator(movies, limit)
    page = request.GET.get('page','1')
    result = paginator.page(page)
    return render(request, 'movies/page_partition_directors.html', {'messages' : result})

@csrf_exempt
def genreRating(request):
    movies=[]
    l1=request.body.find('=')+1
    l2=request.body.find('&')
    l3=request.body.rfind('=')+1
    s1=request.body[l1:l2]
    allMovies = Movie.objects.all()
    dict={}
    for i in range(len(allMovies)):
        dict[allMovies[i].movie_id]=i
    genres = GenresTable.objects.all()
    id=None
    for i in range(len(genres)):
        if genres[i].genres_name==s1:
            id=genres[i].genres_id
    movie = GenreRe.objects.all()
    movies=[]
    for i in range(len(movie)):
        if movie[i].genre_id1==id or movie[i].genre_id2==id or movie[i].genre_id3==id:
            movies.append(allMovies[dict[movie[i].movie_id]])
    s2=request.body[l3:]
    r=Decimal(s2.strip(' "'))
    movie = movies
    dict={}
    for i in range(len(movie)):
        dict[movie[i].movie_id]=(movie[i].primary_title,movie[i].year,movie[i].runtime)
    ratings = Rating.objects.all()
    movies=[]
    for i in range(len(ratings)):
        if ratings[i].average_rating>=r:
            id=ratings[i].movie_id
            if id not in dict:
                continue
            rating=ratings[i].average_rating
            votes=ratings[i].number_of_votes
            movies.append(movie_rating(dict[id][0],dict[id][1],dict[id][2],rating,votes))
    movies.sort(key=lambda x:x.average_rating)
    limit = len(movies)+1
    paginator = Paginator(movies, limit)
    page = request.GET.get('page','1')
    result = paginator.page(page)
    return render(request, 'movies/page_partition_ratings.html', {'messages' : result}) 
