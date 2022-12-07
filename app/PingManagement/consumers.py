import json
from random import randint
import pingparsing
from PingManagement.serializers import PingSerializer
from channels.generic.websocket import WebsocketConsumer

class GraphConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        
        ping_parser = pingparsing.PingParsing()
        transmitter = pingparsing.PingTransmitter()

        transmitter.destination = "8.8.8.8"
        transmitter.count = "10"

        result = ping_parser.parse(transmitter.ping()).as_dict()

        serializer = PingSerializer(data=result)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        
        return json.dumps(result)

       

