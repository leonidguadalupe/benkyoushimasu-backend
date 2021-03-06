import datetime
from collections import defaultdict
from django.db import models
from rest_framework import serializers, exceptions, status
from rest_framework.utils.serializer_helpers import ReturnDict

from api.models import Topic

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ('source', 'topic_type', 'title', 'description')
