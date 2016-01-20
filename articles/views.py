from django.shortcuts import render

from serializers import ArticleSerializer
from models import Article
from rest_framework import generics, viewsets, permissions


# Create your views here.


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    """

    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
