# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movie(models.Model):
	name = models.CharField(max_length=200)
	director = models.CharField(max_length=200)
	score = models.DecimalField(max_digits=3, decimal_places=1)
	popularity = models.DecimalField(max_digits=4, decimal_places=1)


class Genre(models.Model):
	name = models.CharField(max_length=50)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='genres')