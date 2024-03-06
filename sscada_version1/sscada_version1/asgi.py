"""
ASGI config for sscada_version1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# opcua_websocket/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import sscada_version1.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sscada_version1.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            sscada_version1.routing.websocket_urlpatterns
        )
    ),
})
