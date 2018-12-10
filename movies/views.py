# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#django imports
from django.shortcuts import render

#rest_framework imports
from rest_framework import viewsets, filters

#serializers import
from movies.serializers import MovieSerializer, GenreSerializer

#models import
from movies.models import Movie, Genre

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer
	filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
	search_fields = ('name', 'director', 'score', 
					'popularity', 'genres__name')
	ordering_fields = search_fields
	ordering = ('-popularity')


class GenreViewSet(viewsets.ModelViewSet):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer