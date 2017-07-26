# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=100)
    # author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)


