from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.IntegerField()
    message = models.CharField(max_length=1000)
    subject = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
