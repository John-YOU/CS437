# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CastPeople(models.Model):
    person_id = models.TextField(db_column='Person_ID', blank=True, primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    birth_year = models.TextField(db_column='Birth Year', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    death_year = models.TextField(db_column='Death Year', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'cast_people'


class CastRe(models.Model):
    movie_id = models.TextField(db_column='Movie_ID', blank=True, primary_key=True)  # Field name made lowercase.
    person_id = models.TextField(db_column='Person_ID', blank=True, null=True)  # Field name made lowercase.
    characters = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cast_re'


class CrewPeople(models.Model):
    person_id = models.TextField(db_column='Person_ID', blank=True, primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    birth_year = models.TextField(db_column='Birth Year', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    death_year = models.TextField(db_column='Death Year', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    primary_profession = models.TextField(db_column='Primary Profession', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'crew_people'


class CrewRe(models.Model):
    movie_id = models.TextField(db_column='Movie_ID', blank=True, primary_key=True)  # Field name made lowercase.
    person_id = models.TextField(db_column='Person_ID', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crew_re'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GenreRe(models.Model):
    movie_id = models.TextField(db_column='Movie_ID', blank=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    genre_id1 = models.TextField(db_column='genre_ID1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    genre_id2 = models.TextField(db_column='genre_ID2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    genre_id3 = models.TextField(db_column='genre_ID3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'genre_re'


class GenresTable(models.Model):
    genres_name = models.TextField(db_column='Genres_Name', blank=True, null=True)  # Field name made lowercase.
    genres_id = models.TextField(db_column='Genres_ID', blank=True, primary_key=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genres_table'


class Movie(models.Model):
    movie_id = models.TextField(db_column='Movie_ID', blank=True, primary_key=True)  # Field name made lowercase.
    primary_title = models.TextField(db_column='Primary Title', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    isadult = models.IntegerField(db_column='isAdult', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    runtime = models.IntegerField(db_column='Runtime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movie'


class MoviesGenre(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    movie = models.ForeignKey('MoviesMovie', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movies_genre'


class MoviesMovie(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    popularity = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'movies_movie'


class Rating(models.Model):
    x = models.IntegerField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    movie_id = models.TextField(db_column='Movie_ID', blank=True, primary_key=True)  # Field name made lowercase.
    average_rating = models.FloatField(db_column='Average.Rating', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_votes = models.IntegerField(db_column='Number.of.Votes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    level = models.TextField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    popular = models.TextField(db_column='Popular', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rating'


class Title(models.Model):
    movie_id = models.TextField(db_column='Movie_ID', blank=True, null=True)  # Field name made lowercase.
    version_order = models.IntegerField(db_column='Version_order', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    language = models.TextField(db_column='Language', blank=True, null=True)  # Field name made lowercase.
    isoriginaltitle = models.IntegerField(db_column='isOriginalTitle', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'title'
