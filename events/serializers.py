from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from models import Event


# Serializers define the API representation.
class EventSerializer(serializers.ModelSerializer):

    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Event
        fields = ('id', 'title', 'body', 'created', 'date_start', 'date_end', 'image')


# ViewSets define the view behavior.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

