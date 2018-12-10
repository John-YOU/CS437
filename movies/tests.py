# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
import json

from .models import Movie, Genre


def read_json():
	with open("imdb.json") as md:
		movies = json.load(md)

	return movies

def store_data(movies):
	for movie in movies:
		movie_obj = save_movie(movie)
		save_genre(movie_obj, movie["genre"])


def save_movie(movie):
	print movie["name"]
	movie, created = Movie.objects.get_or_create(
		name = movie["name"],
		director = movie["director"],
		score = movie["imdb_score"],
		popularity = movie["99popularity"]
		)
	return movie


def save_genre(movie, genre):
	for gen in genre:
		print gen
		mg = Genre.objects.create(
			name = gen,
			movie = movie
			)
		mg.save()