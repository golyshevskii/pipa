import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    # присоединение пользователя в группу чата
    async def connect(self):
        self.room_group_name = "yami"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    # выход пользователя из чата
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # создание сообщения
    @database_sync_to_async
    def new_message(self, message):
        Message.objects.create(text=message)

    # получение сообщения
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.new_message(message=message)
        await self.channel_layer.group_send(self.room_group_name, {'type': 'chat_message', 'message': message, })

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message, }, ensure_ascii=False))
