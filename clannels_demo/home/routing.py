from django.urls import path
from home.consumers import TestConsumer 


ws_patterns = [
    path('ws/test/', TestConsumer.as_asgi())

]



# acces by WebSocket King: ws://localhost:8000/ws/test/




