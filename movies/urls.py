from django.conf.urls import url
from django.views.generic import ListView, DetailView
from movies.models import Movie
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movies/$', views.movies, name='movies'),
    url(r'^search/$', views.search, name='search'),
    url(r'^show_genres/$', views.show_all_genres, name='show_all_genres'),
]
