import redis
from django.shortcuts import render, HttpResponse
from django_redis import get_redis_connection


def redisIndex(request):
    conn = get_redis_connection("default")
    conn.hset('kkk', 'age', 18)
    return HttpResponse('设置成功')


def redisOrder(request):
    conn = get_redis_connection("default")
    obj = conn.hget('kkk', 'age')
    print(obj)
    return HttpResponse('获取成功')
