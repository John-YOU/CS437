# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#django imports
from django.shortcuts import render

#rest_framework imports
from rest_framework import viewsets, filters

#serializers import
from movies.serializers import MovieSerializer

#models import
from movies.models import MoviesMovie

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
	queryset = MoviesMovie.objects.all()
	serializer_class = MovieSerializer

def index(request):
    return render(request, 'home.html')
