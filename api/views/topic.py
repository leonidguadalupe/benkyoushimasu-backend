"""
.. module:: topic
   :synopsis: Endpoints for topic functionalities
.. moduleauthor:: Leonid Guadalupe <github.com/leonidguadalupe>
"""
from django.http import Http404
from django.db.models import Q
from random import shuffle
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Topic
from api.serializers import TopicSerializer

class TopicViewSet(viewsets.ViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def _get_object(self, id):
        try:
            return Topic.objects.get(id=id)
        except Topic.DoesNotExist:
            raise Http404
    
    @action(detail=True, url_path='topics', url_name='topics', methods=['get'])
    def list(self, request):
        topics = Topic.objects.all()
        serializer = self.serializer_class(topics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def create(self, request):
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        topic = self._get_object(id=pk)
        if pk:
            serializer = serializer_class(topic, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, url_path='update-topic', url_name='update-topic', methods=['put'])
    def update(self, request, pk=None):
        topic = self._get_object(id=pk)
        serializer = serializer_class(topic, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pass

    @action(detail=True, url_path='delete-topic', url_name='delete', methods=['delete'])
    def deactivate(self, request, pk=None):
        topic = self._get_object(id=pk)
        topic.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)
