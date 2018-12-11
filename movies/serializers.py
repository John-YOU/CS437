#rest_framework imports
from rest_framework import serializers

#model imports
from movies.models import MoviesMovie

class MovieSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = MoviesMovie
		fields = ('id','name','director','score','popularity')
