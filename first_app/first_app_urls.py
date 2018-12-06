"""untitled4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from first_app import views as tv

urlpatterns = [

    re_path(r'index/',tv.first_normalmap),
    re_path(r'withparam/(?P<name>[\u4E00-\u9FA5]+|[a-zA-Z]+)/',tv.withparam),
    re_path(r'insideparam/(?:age-(?P<age>\d+))',tv.insideparam),
    re_path(r'ownparam/(?P<old>\d+)',tv.ownparam,{'car':'benz'}),
    re_path(r'nameparam/',tv.nameparam,name = 'kangkang')

]
