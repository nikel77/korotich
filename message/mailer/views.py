from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Message, User
from .serializers import MessageSerializerGet, MessageSerializerPost


class MessageView(APIView):
    def post(self, request):
        message = request.data.get('message')
        serializer = MessageSerializerPost(data=message)
        if serializer.is_valid(raise_exception=True):
            if is_user_valid(message['receiver']) and is_user_valid(message['sender_id']):
                message_saved = serializer.save()
            else:
                return Response('please provide valid id', status=status.HTTP_400_BAD_REQUEST)
        return Response({"id": message_saved.id})


class MessageViewUser(APIView):
    def get(self, request, user_id):
        messages = Message.objects.all().filter(receiver=user_id)
        serializer = MessageSerializerGet(messages, many=True)
        return Response({'user_id': user_id, 'messages': serializer.data})


class MessageViewUnreadUser(APIView):
    def get(self, request, user_id):
        messages = Message.objects.all().filter(receiver=user_id, is_read=False)
        serializer = MessageSerializerGet(messages, many=True)
        return Response({"messages": serializer.data})


class MessageViewMessage(APIView):
    def delete(self, request, message_id):
        message = get_object_or_404(Message.objects.all(), id=message_id)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, message_id):
        message = Message.objects.all().filter(id=message_id)
        serializer = MessageSerializerGet(message, many=True)
        saved_message = get_object_or_404(Message.objects.all(), id=message_id)
        saved_message.is_read = True
        saved_message.save()
        return Response({'message': serializer.data})


def is_user_valid(user_id):
    user = User.objects.all().filter(id=user_id)
    if user:
        return True
    else:
        return False


