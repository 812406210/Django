from django.contrib import admin

# Register your models here.
from django.conf.urls import url
from django.contrib import admin
from . import models

admin.site.register(models.Web)  #这一行注册后，admin就可以管理数据库中这类对象了
