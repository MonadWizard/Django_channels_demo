from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    path('demo/<str:sender>/<str:receiver>/', consumers.DemoConsumer.as_asgi()),

]

#  ws://127.0.0.1:8000/demo/2/
# send :    
# {"data": "what3"}