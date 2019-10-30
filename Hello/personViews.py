import datetime
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
# Create your views here.
from Hello.models import Person

def listPerson(request):
    person = Person.objects.all() #查询所有
    data = {}
    jsonData = serializers.serialize('json',person)
    d = json.loads(jsonData)
    print(type(d),d)
    #data["data"] = json.loads(jsonData)
    return  JsonResponse(d,safe=False)
