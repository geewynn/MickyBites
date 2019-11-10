# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# from django.contrib.auth.models import User
#
# # Create your models here.
#
#
# class UserProfile(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     mobile_number = models.IntegerField()
#
#     def __str__(self):
#         return self.user.username


class Product(models.Model):
    #    owner = models.ForeignKey('auth.User', related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    price = models.IntegerField()
    description = models.CharField(max_length=200, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['date_added']