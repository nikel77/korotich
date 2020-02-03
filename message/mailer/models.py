from datetime import datetime
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.IntegerField()
    message = models.CharField(max_length=1000)
    subject = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=datetime.utcnow)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
