from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def first_normalmap(request):
    print("in normalapp")
    return HttpResponse("first normalapp")
    pass


def withparam(request,year,month):
    print("in withparam")
    return HttpResponse('Today is {}, month is {}'.format(year,month))