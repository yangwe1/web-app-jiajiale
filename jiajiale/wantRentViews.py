# -*- coding=utf-8 -*-

from django.views.generic import ListView, View, TemplateView
from django.shortcuts import HttpResponse, redirect, render, render_to_response
from django.core.urlresolvers import reverse

#from braces.views import JSONResponseMixin
from mongoengine import Q
from models import *

from forms import RentForm

class sale(TemplateView):
    ''' show the index.html '''

    #context_object_name = 'eachInfo'
    template_name = 'wantRent.html'

    def get( self, request, *args, **kwargs ):
        d = request.GET
        eachPageLimit = 12
        eachInfo = eachHouseInfo.objects().limit( eachPageLimit )
        print 'eachInfo : ',eachInfo
        returnData = {
            'eachInfo': eachInfo
        }

        return render_to_response(template_name)

    def post(self, request, *args, **kwargs):
        form = RentForm(request.POST)
        if not form.is_valid():
            print 'invalid form'
            return render_to_response('wantRent.html')

        info = form.cleaned_data
        name = info.get('name')
        phone = info.get('phone')
        cardID = info.get('cardID')
        sex = info.get('sex')
        address = info.get('address')
        districtName = info.get('districtName')
        floorName = info.get('floorName')
        floorNum = info.get('floorNum')
        houseNum = info.get('houseNum')
        houseStyle = info.get('houseStyle')
        houseSqure = info.get('houseSqure')
        useSqure = info.get('useSqure')
        time = info.get('time')
        totalFloor = info.get('totalFloor')

        try:
            eachRentInfo(
                phone = phone,

            ).save()
        except:
            pass

        return redirect(reverse('index'))
