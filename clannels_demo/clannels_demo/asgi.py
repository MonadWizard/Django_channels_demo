import os

# from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from home import routing


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clannels_demo.settings')

# application = get_asgi_application()


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )
})


