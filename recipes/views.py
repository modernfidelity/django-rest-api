from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from serializers import RecipeSerializer
from models import Recipe
from permissions import IsOwnerOrReadOnly

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class RecipeList(generics.ListAPIView):
    """

    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """

    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# ViewSets define the view behavior.
class RecipeViewSet(viewsets.ModelViewSet):
    """

    """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
