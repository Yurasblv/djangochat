from django.contrib.auth.models import User
from rest_framework import serializers
from chat_app.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('user', 'text_message', 'date', 'time')
