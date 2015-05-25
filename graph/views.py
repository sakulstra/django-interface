from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from .models import Sensordata

#rest
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from graph.serializers import UserSerializer, GroupSerializer, SensordataSerializer

def index(request):
    latest_data = Sensordata.objects.order_by('created')[:20]
    graphs = {"current": [], "wind_speed": [], "temperature": [], "wind_direction": [], "precipitation": [], "power": []}
    timestamps = []
    for data in latest_data:
        for graph in graphs:
            graphs[graph].append(getattr(data, graph))
        timestamps.append(data.created.strftime('%H:%M'))#%Y-%m-%d

    context = RequestContext(request, {
        'graphs': graphs,
        'timestamps': timestamps
    })
    return render(request, 'graph/index.html', context)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SensordataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Sensordata.objects.all()
    serializer_class = SensordataSerializer