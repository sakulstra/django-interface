__author__ = 'lukas'

from django.contrib.auth.models import User, Group
from graph.models import Sensordata
from rest_framework import serializers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SensordataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensordata
        fields = ('temperature', 'wind_speed', 'wind_direction', 'precipitation', 'current', 'power')