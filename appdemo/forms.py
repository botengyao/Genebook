# -*- coding:utf-8 -*-

from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password1 = forms.CharField(label='设置密码', max_length=32, widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', max_length=32, widget=forms.PasswordInput())
    full_name = forms.CharField(label='姓名', max_length=32)
    organization = forms.CharField(label='组织名称', max_length=64)
    phone_number = forms.CharField(label='电话号码', max_length=14)