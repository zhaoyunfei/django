"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hello.views import *

urlpatterns = [
    # url(r'^hello/$', hello),
    url(r'^admin/', admin.site.urls),
    url(r'^$','hello.views.showBlogList'),
    url(r'^blog/(\d+)$', 'hello.views.showBlog'),
    url(r'^hello/register', 'hello.views.register'),
    # url(r'^blog/', register),
    # url(r'^regist/$', 'cookie.views.regist'),
    # url(r'^login/$', 'cookie.views.login'),
    # url(r'^index/$', 'cookie.views.index'),
    # url(r'^logout/$', 'cookie.views.logout'),
    url(r'^login/$', 'session.views.login'),
    url(r'^index/$', 'session.views.index'),
    url(r'^logout/$', 'session.views.logout'),

]
