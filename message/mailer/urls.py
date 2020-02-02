from django.urls import path
from .views import MessageView, MessageViewUser, MessageViewUnreadUser, MessageViewMessage


app_name = "mailer"

urlpatterns = [
    path('messages/', MessageView.as_view()),
    path('messages/<int:user_id>/', MessageViewUser.as_view()),
    path('messages/unread/<int:user_id>/', MessageViewUnreadUser.as_view()),
    path('messages/message/<int:message_id>/', MessageViewMessage.as_view()),
    ]
