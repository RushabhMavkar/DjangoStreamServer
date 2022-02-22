from django.db import models
from django.contrib.auth.models import User


class Server(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=256, unique=True, null=True)
    is_secure = models.BooleanField(default=True)
    access = models.CharField(max_length=1024, default="C:\\GATE")
    created_on = models.DateTimeField(auto_now_add=True)


class UserBookmark(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    path = models.CharField(max_length=1024)


class UserAccess(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    server = models.ForeignKey(to=Server, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    activated = models.BooleanField(default=False)
    has_validity = models.BooleanField(default=False)
    valid_till = models.DateTimeField(null=True)
