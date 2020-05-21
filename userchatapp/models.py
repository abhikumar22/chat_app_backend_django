from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

class Auth(models.Model):
    uid = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='authtokens')
    token=models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

class Chat(models.Model):
    senderId = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='sender_user_id')
    receiverId = models.ForeignKey(User,on_delete=models.DO_NOTHING, related_name='receiver_user_id')
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content_of_blog = models.CharField(max_length=255)
    read_interval_in_minutes=models.CharField(max_length=50)
    created_at = models.CharField(max_length=100)