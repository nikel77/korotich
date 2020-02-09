from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Message, User
from .serializers import UserSerializerPost, MessageSerializerGet, MessageSerializerPost
from django.contrib.auth import authenticate, login, logout


class SignupView(APIView):
    def post(self, request):
        req_data = request.data.get('signup_form')
        try:
            User.objects.get(username=req_data['username'])
        except:
            serializer = UserSerializerPost(data=req_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            signed_user = User.objects.get(username=req_data['username'])
            return Response({'user_id': signed_user.id})
        return Response('username already exists', status=status.HTTP_403_FORBIDDEN)


class LoginView(APIView):
    def post(self, request):
        req_data = request.data.get('login_form')
        try:
            user = authenticate(request, username=req_data['username'], password=req_data['password'])
            login(request, user)
            current_user = request.user
        except:
            return Response('please provide valid username and password', status=status.HTTP_403_FORBIDDEN)
        return Response({'user_id': current_user.id})


class LogoutView(APIView):
    def get(self, request):
        current_user = request.user
        logout(request)
        return Response({'user_id': current_user.id})


class MessageView(APIView):
    def post(self, request):
        message = request.data.get('message')
        current_user = request.user
        if not current_user.id:
            return Response('Log in please', status=status.HTTP_400_BAD_REQUEST)
        message['sender_id'] = current_user.id
        serializer = MessageSerializerPost(data=message)
        if serializer.is_valid(raise_exception=True):
            if is_user_valid(message['receiver']):
                message_saved = serializer.save()
            else:
                return Response('please provide valid receiver', status=status.HTTP_400_BAD_REQUEST)
        return Response({"id": message_saved.id})

    def get(self, request):
        current_user = request.user
        if not current_user.id:
            return Response('Log in please', status=status.HTTP_400_BAD_REQUEST)
        messages = Message.objects.all().filter(receiver=current_user.id)
        serializer = MessageSerializerGet(messages, many=True)
        return Response({'messages': serializer.data})


class MessageViewUnread(APIView):
    def get(self, request):
        current_user = request.user
        if not current_user.id:
            return Response('Log in please', status=status.HTTP_400_BAD_REQUEST)
        messages = Message.objects.all().filter(receiver=current_user.id, is_read=False)
        serializer = MessageSerializerGet(messages, many=True)
        return Response({'messages': serializer.data})


class MessageViewMessage(APIView):
    def get(self, request, message_id):
        message = Message.objects.get(pk=message_id)
        serializer = MessageSerializerGet(message)
        current_user = request.user
        if not current_user.id:
            return Response('Log in please', status=status.HTTP_400_BAD_REQUEST)
        if message.receiver == current_user.id:
            message.is_read = True
            message.save()
            return Response({'message': serializer.data})
        else:
            return Response('You have no rights to read this message', status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, message_id):
        current_user = request.user
        if not current_user.id:
            return Response('Log in please', status=status.HTTP_403_FORBIDDEN)
        message = get_object_or_404(Message.objects.all(), id=message_id)
        if message.receiver == current_user.id or message.sender_id == current_user.id:
            message.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('You have no rights to delete this message', status=status.HTTP_403_FORBIDDEN)


def is_user_valid(user_id):
    try:
        User.objects.get(pk=user_id)
    except:
        return False
    return True
