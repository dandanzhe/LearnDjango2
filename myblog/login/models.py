#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Uer(models.Model):
    name = models.CharField(max_length=32)
    passwd = models.TextField()
    email = models.EmailField()
    # admin 显示标题
    def __unicode__(self):
        return self.title
