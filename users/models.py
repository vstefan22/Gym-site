from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    user_progress = models.IntegerField(default = 0)

class Membership(models.Model):
    account = models.ForeignKey(Account, on_delete = models.CASCADE)
    date = models.DateField()
    plan = models.CharField(max_length = 100, null = True, blank = True)
