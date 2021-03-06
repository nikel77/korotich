from django.urls import path
from .views import SignupView, LoginView, LogoutView, MessageView, MessageViewUnread, MessageViewMessage


app_name = "mailer"

urlpatterns = [
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('messages', MessageView.as_view()),
    path('messages/unread', MessageViewUnread.as_view()),
    path('messages/<int:message_id>', MessageViewMessage.as_view()),
    ]
