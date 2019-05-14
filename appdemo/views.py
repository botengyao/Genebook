# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import UserForm
from .models import UserProfile
from django.contrib import auth
from django.contrib.auth.hashers import check_password


# Create your views here.
# from django.contrib.auth.decorators import login_required
# @login_required(login_url='login/')

def index(request):
    return render(request, 'index.html')


# 用户登陆网页
def login(request):
    return render(request, 'login.html')


# 用户注册网页
def register(request):
    return render(request, 'register.html')


def logout(request):
    # 清除当前对应session所有数据
    request.session.clear()
    # 或者 auth.logout(request)
    return render(request, 'logout.html')


# 用户登陆认证逻辑
def login_auth(request):
    try:
        usr = request.GET['usr']
        pwd = request.GET['pwd']
        user = authenticate(username=usr, password=pwd)
        staff_status = user.is_staff
        # 密码确认，此处没有使用，只是在debug时用到
        print(check_password(request.GET.get('pwd'), user.password))
        if user is not None and staff_status:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        elif user is not None and not staff_status:
            return HttpResponse(
                "<br>Please contact the administrator to confirm the account! Administrator email: <a href='mailto:tsl-zhangwen0@tasly.com'><strong>tsl-zhangwen0@tasly.com!</strong></a>")
        else:
            print(user)
            return render(request, "login_error.html")
    except:
        return render(request, "login_error.html")


# 用户提交注册逻辑
def register_commit(request):
    try:
        form = UserForm(request.POST)
        # 获取表单信息
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                return HttpResponse("Inconsistent password!")
            else:
                full_name = form.cleaned_data['full_name']
                organization = form.cleaned_data['organization']
                phone_number = form.cleaned_data['phone_number']
                # 将表单写入数据库
                user = UserProfile.objects.create_user(username=username, password=password1, full_name=full_name,
                                                       organization=organization, phone_number=phone_number)
                user.save()
                return render(request, "register_back.html")
    except:
        return HttpResponse(
            "Sorry, your registration failed.<br>Please contact the administrator to confirm the account! Administrator email: <a href='mailto:tsl-zhangwen0@tasly.com'><strong>tsl-zhangwen0@tasly.com!</strong></a>")


# Create your views here.
def upload_file(request):
    # 请求方法为POST时，进行处理
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，则默认为None
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("没有需要上传的文件")
        else:
            #打开特定的文件进行二进制的写操作
            #print(os.path.exists('/temp_file/'))
            with open("./appdemo/temp_file/%s" % File.name, 'wb+') as f:
                #分块写入文件
                for chunk in  File.chunks():
                    f.write(chunk)
            return HttpResponse("UPload over!")
    else:
        return  render(request, "upload.html")

@login_required
def biodb_auth(request):
    username = request.session.get('user', '')
    print(username)
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    return HttpResponseRedirect("http://tcm.tasly.com:3842")


@login_required
def gwasmed_auth(request):
    username = request.session.get('user', '')
    print(username)
    print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
    return HttpResponseRedirect("/upload_file")


@login_required
def netpred_auth(request):
    username = request.session.get('user', 'tsl-zhangwen0@tasly.com')
    print(username)
    print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
    return HttpResponseRedirect("http://tcm.tasly.com:3843")

