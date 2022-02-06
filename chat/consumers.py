from channels.generic.websocket import WebsocketConsumer

from chat.tasks import message_bot


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        message_bot.delay()
        pass

    def receive(self, text_data=None, bytes_data=None):
        print(text_data)

        self.send(self.channel_name)
