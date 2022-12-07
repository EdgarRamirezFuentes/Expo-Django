import json
from random import randint
from time import sleep
import pingparsing
from PingManagement.serializers import PingSerializer
from channels.generic.websocket import WebsocketConsumer

class GraphConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        
        ping_parser = pingparsing.PingParsing()
        transmitter = pingparsing.PingTransmitter()

        transmitter.destination = "8.8.8.8"
        transmitter.count = 5

        for i in range(10):
            result = ping_parser.parse(transmitter.ping()).as_dict()
            serializer = PingSerializer(data=result)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            self.send(json.dumps(serializer.data))
            

       

