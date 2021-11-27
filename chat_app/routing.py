from chat_app.consumer import ChatConsumer
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer.as_asgi())
]
