from django.urls import path
import chat.consumers

ws_urlpatterns = [
    path("ws/chat/", chat.consumers.ChatConsumer.as_asgi(), name="ws_chat"),
]
