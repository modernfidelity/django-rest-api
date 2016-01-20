from django.conf.urls import url, include
from rest_framework import serializers
from models import Recipe
from django.contrib.auth.models import User


# Serializers define the API representation.
class RecipeSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Recipe
        fields = ('id', 'owner', 'created', 'title', 'strapline', 'instructions')


# Users
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(queryset=Recipe.objects.all(), view_name='recipe-detail',
                                                   many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'recipe')
