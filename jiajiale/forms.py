# -*- coding=utf-8 -*-

from django import forms
from django.contrib import auth
from models import *

import re
from django.contrib.auth.models import User
# from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist


class RentForm(forms.Form):
    ''' 出租房屋验证表单 '''

    GENDER_CHOICES =  (('', '请选择'),('男', '男'),('女', '女'),)
    name = forms.CharField(min_length=1, max_length=20)
    phone = forms.CharField(min_length=7, max_length=20)
    cardID = forms.CharField(min_length=17, max_length=18)
    sex = forms.ChoiceField(required=False, choices=GENDER_CHOICES)
    address = forms.CharField(min_length=1, max_length=20)
    districtName = forms.CharField(min_length=1, max_length=20)
    floorName = forms.CharField(min_length=1, max_length=20)
    floorNum = forms.CharField(min_length=1, max_length=20)
    houseNum = forms.CharField(min_length=1, max_length=20)
    houseStyle = forms.CharField(min_length=1, max_length=20)
    houseSqure = forms.FloatField(min_value=0)
    useSqure = forms.FloatField(min_value=0)
    time = forms.DateField()
    totalFloor = forms.IntegerField(required=False)

    def clean_username(self):
        name = self.cleaned_data.get('name', '')

        if not re.search(u'^[_a-zA-Z0-9\u4e00-\u9fa5]+$',name):
            raise forms.ValidationError('用户名中只能包含字母、数字、下划线和汉字。')
        # name_list = ['root',u'官方','admin']
        # for each_name in name_list:
        #     if each_name in username:
        #         raise forms.ValidationError('该用户名已存在，请重新填写！')
        # try:
        #     #判断用户名是否被注册
        #     User.objects.get(username=username)
        # except ObjectDoesNotExist:
        #     return username
        # raise forms.ValidationError('该用户名已存在，请重新填写！')
        # if len(username) > 20:
        #     raise forms.ValidationError(u'名字太长也不一定有内涵呀 :)')
        return name

    def clean_mobile(self):
        phone = self.cleaned_data.get('phone','')
        if not re.search(u'^[0-9]+$',phone):
            raise forms.ValidationError('输入格式不正确，只能包含数字。')
        return phone

    def clean_cardID(self):
        cardID = self.cleaned_data.get('cardID','')
        if not re.search(u'^[0-9]+$',cardID):
            raise forms.ValidationError('输入格式不正确，只能包含数字。')
        return cardID




class SaleForm(forms.Form):
    ''' 出售房屋验证表单 '''
    pass


