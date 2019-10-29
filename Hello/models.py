from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
from django.db import models
#实体对象

class Web(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    score = models.CharField(max_length=20)

