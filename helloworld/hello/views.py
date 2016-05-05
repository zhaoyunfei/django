from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,JsonResponse,FileResponse
from django.template import loader
from .models import Blog
from django import forms
# Create your views here.
from django.shortcuts import render_to_response
from hello.models import User

# def hello(request):
#     return render_to_response('test.html')
def showBlog(request,blogId):
    t=loader.get_template('blog.html')
    blog=Blog.objects.get(id=blogId)
    context={'blog':blog}
    html=t.render(context)
    return HttpResponse(html)


def showBlogList(request):
    t=loader.get_template('blog_list.html')
    blog_list=Blog.objects.all()
    context={'blog_list':blog_list}
    html=t.render(context)
    return HttpResponse(html)


class UserForm(forms.Form):
    name=forms.CharField()
    headImg=forms.FileField()


def register(request):
    if request.method=='POST':
        form=UserForm(request.POST,request.FILES)
        if form.is_valid():
            # print form.cleaned_data
            # filePath=file('upload/'+form.cleaned_data['headImg'].name,'wb')
            # s=form.cleaned_data['headImg'].read()
            # filePath.write(s)
            # filePath.close()
            name=form.cleaned_data['name']
            headImg=form.cleaned_data['headImg']
            print name,headImg
            user=User()
            user.name=name
            user.headImg=headImg
            user.save()
            return HttpResponse('ok')
    else:
        form=UserForm()
    return render_to_response('register.html',{'form':form})

# from django.contrib import auth
# def login(request):
#     username=request.POST['username']
#     password=request.POST['password']
#     user=auth.authenticate(username=username,password=password)
#     if user is not None:
#         auth.login(request,user)
#         return HttpResponseRedirect('/hello/')
#     else:
#         return render_to_response('login.html',{'err':'login error'})