from django.db import models
from django.contrib.auth.models import User


class Server(models.Model):
    admin = models.ForeignKey(to=User, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=256)
    is_secure = models.BooleanField(default=True)
    access = models.CharField(max_length=1024, default="C:\\GATE")


class UserBookmark(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    path = models.FilePathField()


class UserAccess(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    server = models.ForeignKey(to=Server, on_delete=models.DO_NOTHING)
    has_validity = models.BooleanField(default=False)
    valid_till = models.DateTimeField()
