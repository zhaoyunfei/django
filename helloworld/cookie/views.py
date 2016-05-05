from django.shortcuts import render
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Users

# Create your views here.
class UserForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


def regist(request):
    if request.method=="POST":
        uf=UserForm(request.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            # print username,password
            Users.objects.create(username=username,password=password)
            # return HttpResponse('OK')
            return HttpResponseRedirect('/login/')
    else:
        uf=UserForm()
    return render_to_response('regist.html',{'uf':uf})



def login(request):
    if request.method=="POST":
        uf=UserForm(request.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            # print username,password
            user = Users.objects.filter(username__exact=username,password__exact=password)
            if user:
                # ceshi
                response=HttpResponseRedirect('/index/')
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf=UserForm()
        return render_to_response('login.html',{'uf':uf})


def index(request):
    username=request.COOKIES.get('username','')
    return render_to_response('index.html',{'username':username})


def logout(request):
    response=HttpResponse('logout')
    response.delete_cookie('username')
    return response
