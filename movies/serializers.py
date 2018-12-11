#rest_framework imports
from rest_framework import serializers

#model imports
from movies.models import Movie

class MovieSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Movie
		fields = ('movie_id','primary_title','isadult','year','runtime')
