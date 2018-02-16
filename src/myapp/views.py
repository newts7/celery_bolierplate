from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from celery.decorators import task, periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
import json
import time
# Create your views here.
logger = get_task_logger('_app_')


@csrf_exempt
def index(request):
    d={}
    d['message']="hello"
    add.delay(1,2)
    myperiodic_function()
    return HttpResponse({json.dumps(d)},status=200)


@task(name="sum_two_numbers")
def add(x,y):
    z= x+y
    print("Sum is ",z)
    return x+y


@periodic_task(
    name="My periodic task",
    run_every =  (crontab(minute='*/1')),
    ignore_result= True)
def myperiodic_function():
    print(time.time())
    return
