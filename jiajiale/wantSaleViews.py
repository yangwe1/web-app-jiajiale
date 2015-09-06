# -*- coding=utf-8 -*-

from django.views.generic import ListView, View, TemplateView
from django.shortcuts import HttpResponse, redirect,render
from django.core.urlresolvers import reverse

#from braces.views import JSONResponseMixin
from mongoengine import Q

from models import eachHouseInfo 

class sale(TemplateView):
    ''' show the index.html '''

    #context_object_name = 'eachInfo'
    template_name = 'wantSale.html'
    '''
    def get( self, request, *args, **kwargs ):
        d = request.GET
        eachPageLimit = 12
        eachInfo = eachHouseInfo.objects().limit( eachPageLimit )
        print 'eachInfo : ',eachInfo
        returnData = {
            'eachInfo': eachInfo
        }
        
        return render( request, 'index.html', returnData )
    '''
