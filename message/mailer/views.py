from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Message
from .serializers import MessageSerializerGet, MessageSerializerPost


class MessageView(APIView):
    def post(self, request):
        message = request.data.get('message')
        serializer = MessageSerializerPost(data=message)
        if serializer.is_valid(raise_exception=True):
            message_saved = serializer.save()
        return Response({"success": f"Message with subject '{message_saved.subject}' is created successfully"})


class MessageViewUser(APIView):
    def get(self, request, user_id):
        messages = Message.objects.all().filter(receiver=user_id)
        serializer = MessageSerializerGet(messages, many=True)
        return Response({f"messages of user with id '{user_id}'": serializer.data})


class MessageViewUnreadUser(APIView):
    def get(self, request, user_id):
        messages = Message.objects.all().filter(receiver=user_id, is_read=False)
        serializer = MessageSerializerGet(messages, many=True)
        return Response({"messages": serializer.data})


class MessageViewMessage(APIView):
    def delete(self, request, message_id):
        message = get_object_or_404(Message.objects.all(), id=message_id)
        message.delete()
        return Response({"message": f"message with id '{message_id}' has been deleted"})

    def get(self, request, message_id):
        message = Message.objects.all().filter(id=message_id)
        serializer = MessageSerializerGet(message, many=True)
        saved_message = get_object_or_404(Message.objects.all(), id=message_id)
        saved_message.is_read = True
        saved_message.save()
        return Response({f"message with id '{message_id}'": serializer.data})
