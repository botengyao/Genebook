# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=32, null=True, verbose_name='FullName')
    organization = models.CharField(max_length=64, null=True, verbose_name='Organization')
    phone_number = models.CharField(max_length=14, null=True, verbose_name='PhoneNumber')
