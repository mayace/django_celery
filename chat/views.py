from django.http import JsonResponse
from django.shortcuts import render

from chat.models import Message
from django.views import View
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()


class IndexView(View):
    def get(self, request):
        return render(
            request,
            "chat/index.html",
            {
                "message_list": Message.objects.all(),
            },
        )

    def post(self, request):
        text = request.POST.get("text")

        if text:
            message = Message.objects.create(text=text)

            # async_to_sync(channel_layer.send)(
            #     "",
            #     {
            #         "type": "messages",
            #         "text": message,
            #     },
            # )

            return JsonResponse(
                {
                    "success": True,
                    "data": message.id,
                }
            )

        return self.get(request)


def test(request):
    return render(request, "chat/test.html")
