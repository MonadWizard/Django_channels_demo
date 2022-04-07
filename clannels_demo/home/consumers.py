import json
from channels.generic.websocket import AsyncWebsocketConsumer


class DemoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sender = self.scope['url_route']['kwargs']['sender']
        self.receiver = self.scope['url_route']['kwargs']['receiver']
        self.room_name = self.sender + '_' + self.receiver
        self.room_group_name = 'demo_' + self.room_name

        # when Shaon joins the room
        # Shaon_Rakib, demo_shaon_rakib
        # when Rakib joins the room
        # Rakib_Shaon, demo_rakib_shaon
        # meta_table_name = {user1: Shaon, user2: Rakib, table_name='something2022'}
        # meta_table_name = {user1: Rakib, user2: Shaon, table_name='something2022'}
        # meta_chat = {user1, user2, table_name}
        # something2022 = {sender, receiver, message, date_time, is_deleted, is_seen}

        print('room_name: ' + self.room_name)
        print('room_group_name: ' + self.room_group_name)

        # Join room group
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()

        # call meta table with user1, user2
        # if this data exist return table_name
        # if don't then create table and return table_name

        # a function will be called
        # which will get previous messages data from database
        # this function will be async
        data = [
            {'user':'Shaon','message': 'hello', 'date_time': '2020-01-01 16:00:00'},
            {'user':'Rakib','message': 'Hi, how are you?', 'date_time': '2020-01-01 16:00:00'},
            {'user':'Shaon','message': 'Im am fine', 'date_time': '2020-01-01 16:00:00'},  
            {'user':'Shaon','message': 'How are you?', 'date_time': '2020-01-01 16:00:00'},  
            {'user':'Shaon','message': '*I am', 'date_time': '2020-01-01 16:00:00'},
        ]
        # ws://base-url/demo/sender-user-id/receiver-user-id/

        await self.send(text_data=json.dumps({
            'success': True,
            'data': data,
        }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        taking_data = text_data_json['data']

        if text_data_json['data'] == 'resend':
            page = text_data_json['page']
            # an async function will be called
            # which will actually behave like pagination
            data_user1 = {
                "message_1": {'user':'Shaon','message': 'hello', 'date_time': '2020-01-01 16:00:00'},
                "message_2": {'user':'Rakib','message': 'Hi, how are you?', 'date_time': '2020-01-01 16:00:00'},
            }
        else:
            user = self.sender
            data = {
                "message_1": 
                    {"user": user,"message": text_data_json['data'],"date_time": "2020-01-01 16:00:00"}
                }
            
            data_user1 = 'message-sent'
        
            self.room_name_temp = self.receiver + '_' + self.sender
            self.room_group_name_temp = 'demo_' + self.room_name_temp

            await self.channel_layer.group_send(self.room_group_name_temp,{
                'type': 'send_demo_data',
                'data': data,
            })

        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'send_demo_data',
            'data': data_user1,
        })

        

    async def send_demo_data(self, event):
        data = event['data']
        print('event data:::: ', data)

        await self.send(text_data=json.dumps({
            'data': data,
        }))


