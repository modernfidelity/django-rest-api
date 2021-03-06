# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.response import Response

from rest_framework import generics, viewsets, permissions
from serializers import EventSerializer
from models import Event
# from permissions import IsOwnerOrReadOnly


# Create your views here.

#
# @api_view(['GET', 'POST'])
# @permission_classes((AllowAny,))
# def event_list(request, format=None):
#     """
#     List all events, or create a new event.
#     """
#     if request.method == 'GET':
#         events = Event.objects.all()
#         serializer = EventSerializer(events, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = EventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def event_detail(request, pk, format=None):
#     """
#      Retrieve, update or delete a event instance.
#     """
#
#     try:
#         event = Event.objects.get(pk=pk)
#     except Event.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = EventSerializer(event)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = EventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         event.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




class EventList(generics.ListAPIView):
    """
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# ViewSets define the view behavior.
class EventViewSet(viewsets.ModelViewSet):
    """
    Event content type viewset default
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
