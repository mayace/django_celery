from celery import shared_task
from chat.models import Message


@shared_task
def message_bot():
    return "bruh"


@shared_task
def check_messages():
    messages = Message.objects.filter(
        checked=False,
    )

    for item in messages:
        item.checked = True
        item.save()

    return messages.count()