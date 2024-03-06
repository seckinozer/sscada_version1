from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from scada_plc_control.consumers import PLCConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/sscada_version1/', PLCConsumer.as_asgi()),
    ]),
})