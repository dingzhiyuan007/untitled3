from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.


def first_normalmap(request):
    print("in normalapp")
    return HttpResponse("这是主页")
    pass


def withparam(request,name):
    print("in withparam")
    return HttpResponse('Today is {}'.format(name))

def insideparam(request,age):
    print("in insideparam")
    return HttpResponse('I am {} old.'.format(age))

def ownparam(request,old,car):
    print("in ownparam")
    return HttpResponse('car is {},old is {}'.format(car,old))

def nameparam(requset):
    print("in nameparam")
    return HttpResponse('This is {}'.format(reverse("kangkang")))