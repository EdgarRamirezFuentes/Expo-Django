from rest_framework import (
    viewsets,
    views,
    response,
)
import json 
from .serializers import PingSerializer
from core.models import Ping
from django.shortcuts import render
import pingparsing
from datetime import (
    date,
    datetime
)

def index(request):
    return render(request, 'base.html', context = {'text': 'HI'})

class PingViewset(viewsets.ModelViewSet):
    serializer_class = PingSerializer
    queryset = Ping.objects.all()


class PinggerView(views.APIView):
    def get(self, request, destination, count):
        ping_parser = pingparsing.PingParsing()
        transmitter = pingparsing.PingTransmitter()

        transmitter.destination = destination
        transmitter.count = count 

        result = ping_parser.parse(transmitter.ping()).as_dict()

        serializer = PingSerializer(data=result)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        

        print(result)

        return response.Response(serializer.data)


