from rest_framework import serializers
from .models import Message
from datetime import datetime


class MessageSerializerPost(serializers.Serializer):
    sender_id = serializers.IntegerField()
    receiver = serializers.IntegerField()
    message = serializers.CharField(max_length=1000)
    subject = serializers.CharField(max_length=100)
    creation_date = serializers.DateTimeField(default=datetime.utcnow)
    is_read = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Message.objects.create(**validated_data)


class MessageSerializerGet(MessageSerializerPost):
    id = serializers.IntegerField()

