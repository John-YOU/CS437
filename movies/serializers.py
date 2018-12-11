#rest_framework imports
from rest_framework import serializers

#model imports
from movies.models import Movie, GenresTable

class GenresTableSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = GenresTable
		fields = ('genres_name','genres_id','description')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Movie
		fields = ('movie_id','primary_title','isadult','year','runtime')
