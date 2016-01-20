from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from models import Article


# Serializers define the API representation.
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'strapline')


# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer