from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task
import logging
from chat_app.models import Message

logger = logging.getLogger()

channel_layer = get_channel_layer()


@shared_task()
def send_message_task(room_name, message):
    async_to_sync(channel_layer.group_send(room_name,
                                           {'type': 'chat_message', 'message': message})
                  )
