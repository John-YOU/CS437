from django.conf.urls import url
from django.views.generic import ListView, DetailView
from movies.models import Movie
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^moviesInfo$', views.moviesInfo, name='moviesInfo'),
    url(r'^rating$', views.rating, name='rating'),
    url(r'^popularity$',views.popularity,name='popularity'),
    url(r'^movies/$', views.movies, name='movies'),
    url(r'^search/$', views.search, name='search'),
    url(r'^genres/$', views.genres, name='genres'),
]
