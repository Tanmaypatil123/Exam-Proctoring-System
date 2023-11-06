import json
from channels.generic.websocket import AsyncWebsocketConsumer 
from asgiref.sync import async_to_sync 
from django.contrib.auth.models import User
from time import sleep
import datetime
from channels.db import database_sync_to_async


class ConnectUser(AsyncWebsocketConsumer):
    async def connect(self):
        print(f"================== {self.scope['user']}")
        await self.accept() 
        await self.channel_layer.group_add(f"mychat_app_{self.scope['user']}", self.channel_name)

    async def disconnect(self, close_code): 
        # store log user get disconnect
        pass

    async def receive(self, text_data):
        text_data = json.loads(text_data)
        await self.channel_layer.group_send(
                f"mychat_app_{text_data['user']}",
                {
                    'type':'send.msg',
                    'msg':"pass the data which want to send"
                }
            )
        # proccess the incoming data
    
    async def send_msg(self,event):
        print(event['msg'])
        await  self.send(event['msg'])