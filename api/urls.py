"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework import routers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from settings import API_VERSION, DEBUG

from events.views import EventViewSet
from recipes.views import RecipeViewSet
from articles.views import ArticleViewSet

@api_view(['GET'])
@permission_classes((AllowAny,))
def get_api_version(request):
    return Response({API_VERSION})


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [

    # Generics
    url(r'^version', get_api_version, name='get_api_version'),
    url(r'^', include(router.urls)),

    # Admin
    url(r'^admin/', admin.site.urls),

    # Docs
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),

    # JWT Auth Token
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),

]

# On DEV server serve the local media files
if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
