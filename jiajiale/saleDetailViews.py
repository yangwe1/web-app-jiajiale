# -*- coding=utf-8 -*-
# author guiche
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import HttpResponse, redirect, render
from django.shortcuts import render_to_response

from models import eachHouseInfo

class getEachDetailInfo( View ):

    context_object_name = 'eachInfo'

    def get( self, request, *args, **kwargs ):

        d = request.GET

        self.eachID = d.get( 'eachID' )
        print 'eachID :', self.eachID
        print 'typeof eachID :',type( self.eachID )
        eachInfo = eachHouseInfo.objects( id = self.eachID  )
        print 'eachInfo: ',eachInfo
        returnData = {
            'eachInfo': eachInfo
        }

        return render( request,'saleDetail.html',returnData)

