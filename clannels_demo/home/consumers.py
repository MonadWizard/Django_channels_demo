import json
from channels.generic.websocket import AsyncWebsocketConsumer


class DemoTransactionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['id']
        self.room_group_name = 'demo_transaction_' + self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()

        await self.send(text_data=json.dumps(
            {
                'success': True,
                'message': 'Connected to ' + self.room_group_name + ' group',
            }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        data = text_data_json['data']

        print('data received: ' + json.dumps(data))

        # self.target_room_group_name = 'demo_transaction_' + self.room_name

        # await self.channel_layer.group_send(self.target_room_group_name, {
        #     'type': 'send_demo_transaction_data',
        #     'data': data,
        # })

    # or 
        await self.channel_layer.group_send(self.room_group_name, 
        {
            'type': 'send_demo_transaction_data',
            'data': data,
        })

    # Receive message from room group
    async def send_demo_transaction_data(self, event):
        data = event['data']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'data': data,
        }))


