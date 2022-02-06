"""
ASGI config for clannels_demo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import home.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clannels_demo.settings')

application = get_asgi_application()


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            home.routing.ws_patterns
        )
    )
})


