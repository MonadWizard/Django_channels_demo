from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    # re_path(r'transactoin_proc', consumers.DemoTransactionConsumer.as_asgi()),
    # re_path(r'transaction_proc/(?P<id>\w+)/$',consumers.DemoTransactionConsumer.as_asgi()),
    path('transaction_proc/<str:id>/', consumers.DemoTransactionConsumer.as_asgi()),


]

#  ws://127.0.0.1:8000/transaction_proc/2/
# send :    
# {"data": "what3"}