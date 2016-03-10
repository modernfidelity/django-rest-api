from django.shortcuts import render

from rest_framework import generics, viewsets, permissions
from serializers import ArticleSerializer
from models import Article
from permissions import IsOwnerOrReadOnly

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

# Create your views here.


class ArticleList(generics.ListAPIView):
    """
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    """
    Article content type viewset default
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')