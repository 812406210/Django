# Create your models here.
# -*- coding: utf-8 -*-
from django.db import models
#实体对象
'''
测试实体对象
'''
class Web(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    score = models.CharField(max_length=20)

'''
实体对象
'''
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=20)
    sage = models.IntegerField()
    sscore = models.CharField(max_length=20)

