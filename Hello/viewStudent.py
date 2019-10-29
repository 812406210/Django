import datetime
import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
# Create your views here.
from django.urls import reverse

from Hello.models import Web


def sayHello(request):
    s = 'Hello World!'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)

def showStudents(request):
    list = [{id: 1, 'name': 'Jack'}, {id: 2, 'name': 'Rose'}]
    return render_to_response('hello.html',{'students': list})

'''
查询所有
'''
def showStudents(request):
    list = Web.objects.all()#查询所有
    return render_to_response('hello.html',{'students': list})


'''
根据条件查询
'''
def showStudentsByKey(request,*args):
    list = Web.objects.filter(id=9)
    print(list)
    return render_to_response('hello.html',{'students': list})

'''
保存数据
'''
def addStudent(request):
    for i in range(100):
        db_obj = Web(name="yangqian"+str(i),score="100"+str(i),age=18+i)
        db_obj.save()
    return  render_to_response('home.html')

'''
保存数据,入参为json数据
'''
def addStudentByJson(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body) #将json转为字典
        print(received_json_data)
        web = Web(**json.loads(request.body))#将json转为models对象
        web.save()#保存入库
        print('成功！！！！')
    else:
        print('abc')
    #重定向到Home界面
    return  render_to_response('home.html')


'''
根据Key删除数据
url: http://127.0.0.1:8000/deleteStudentByKey/6
'''
def deleteStudentByKey(request,id):
    #id = request.GET["id"]
    obj = Web.objects.get(id=id)
    if obj:
        #删除
        obj.delete()
        return  render_to_response('Home.html')
    else:
        return HttpResponse(u"删除失败")

"""
根据Key去修改
"""
def updateStudentInfoByKey(request,id):
    #方式二:推荐使用
    Web.objects.filter(id=id).update(name="bbbbbbc",age=1000)
    return HttpResponse(u"修改成功")

"""
1、自定义sql语句
2、返回Json字符串
"""
def handsWriteSql(request):
    obj = Web.objects.raw("select * from hello_web where  id  = 11 ")
    data = {}
    province = serializers.serialize("json", obj)
    data["data"] = json.loads(province)
    print(data)
    return JsonResponse(data, safe=False)




