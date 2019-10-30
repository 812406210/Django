"""Django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys
sys.path.append("..")   #python文件引入
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from Hello import viewStudent
from Hello import redisViews
from Hello import personViews
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello/', viewStudent.sayHello),    #路径映射
    url(r'^showStudents/$', viewStudent.showStudents),
    url(r'^showStudentsByKey/$', viewStudent.showStudentsByKey),
    url(r'^addStudent/$', viewStudent.addStudent),
    url(r'^addStudentByJson/$', viewStudent.addStudentByJson),
    url(r'^deleteStudentByKey/(?P<id>\d+)', viewStudent.deleteStudentByKey),
    url(r'^updateStudentInfoByKey/(?P<id>\d+)', viewStudent.updateStudentInfoByKey),
    url(r'^handsWriteSql/$', viewStudent.handsWriteSql),


    url(r'^redisIndex/$', redisViews.redisIndex),
    url(r'^redisOrder/$', redisViews.redisOrder),



    url(r'^listPerson/$', personViews.listPerson),


]


