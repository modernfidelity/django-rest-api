from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from articles import views

urlpatterns = [
    url(r'^api/$', views.ArticleList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
