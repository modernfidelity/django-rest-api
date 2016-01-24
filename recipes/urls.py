from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from recipes import views

urlpatterns = [
    url(r'^api/$', views.RecipeList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.RecipeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
