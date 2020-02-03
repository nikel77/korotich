from django.urls import path
from .views import MessageView, MessageViewUser, MessageViewUnreadUser, MessageViewMessage


app_name = "mailer"

urlpatterns = [
    path('messages', MessageView.as_view()),
    path('users/<int:user_id>/messages', MessageViewUser.as_view()),
    path('users/<int:user_id>/messages/unread', MessageViewUnreadUser.as_view()),
    path('messages/<int:message_id>', MessageViewMessage.as_view()),
    ]
