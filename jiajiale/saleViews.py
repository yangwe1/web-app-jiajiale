# -*- coding=utf-8 -*-
# author guiche
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import HttpResponse, redirect, render
from django.shortcuts import render_to_response
#from django.template import Template
from mongoengine import Q

from models import eachHouseInfo 

class getSaleList( View ):

    context_object_name = 'eachInfo'
    template_name = 'sale.html'

    def get( self, request, *args, **kwargs ):

        d = request.GET

        self.page = d.get( 'page' )
        self.district = d.get( 'district' )
        self.sort = d.get( 'sort' )
        self.apartment = d.get( 'apartment' )
        self.ltPrice = d.get( 'ltPrice' )
        self.gtPrice = d.get( 'gtPrice' )
        print 'self.district :',self.district
        print 'self.sort :',self.sort
        print 'self.apartment :',self.apartment
        print 'self.ltPrice :',self.ltPrice
        print 'self.gtPrice :',self.gtPrice
        if not self.sort:
            self.sort = u""
        if not self.district:
            self.district = u""

        sorts = [
            u"",
            u"新房",
            u"二手房",
            u"办公写字楼",
            u"店面商铺",
            u"平房/独院/地皮",
            u"厂房/仓库/车库",
            u"别墅",
            u"其他房讯"
        ]

        districts = [
            u"",
            u"市区",
            u"郊区",
            u"开发区",
            u"博昌",
            u"锦秋",
            u"湖滨",
            u"店子",
            u"兴福",
            u"曹王",
            u"陈户",
            u"吕艺",
            u"庞家",
            u"纯化",
            u"乔庄",
            u"其他"
        ]

        apartments = [
            {'num':0,'name':u""},
            {'num':1,'name':u"一室"},
            {'num':2,'name':u"两室"},
            {'num':3,'name':u"三室"},
            {'num':4,'name':u"四室"},
            {'num':5,'name':u"四室以上"}
        ]

        prices = [
            {'gtPrice':0,  'ltPrice':0,'name':u""},
            {'gtPrice':0,  'ltPrice':10,'name':u"10万以下"},
            {'gtPrice':10, 'ltPrice':20,'name':u"10万-20万"},
            {'gtPrice':20, 'ltPrice':30,'name':u"20万-30万"},
            {'gtPrice':30, 'ltPrice':40,'name':u"30万-40万"},
            {'gtPrice':40, 'ltPrice':50,'name':u"40万-50万"},
            {'gtPrice':50, 'ltPrice':60,'name':u"50万-60万"},
            {'gtPrice':60, 'ltPrice':80,'name':u"60万-80万"},
            {'gtPrice':80, 'ltPrice':100,'name':u"80万-100万"},
            {'gtPrice':100,'ltPrice':150,'name':u"100万-150万"},
            {'gtPrice':150,'ltPrice':200,'name':u"150万-200万"},
            {'gtPrice':200,'ltPrice':2000,'name':u"200万以上"},
        ]
        
        search,intApartment,intLtPrice,intGtPrice = dealWithSearch( self.district,self.sort,self.apartment,self.ltPrice,self.gtPrice )

        print 'search: ',search
        pageNum = 1 
        if self.page and self.page.isalnum(): 
            pageNum = max( 1, int(self.page) )
        print 'pageNum: ',pageNum
        eachPageLimit = 24 
        skip = ( pageNum -1 ) * eachPageLimit
        count = eachHouseInfo.objects( **search ).count()
        print 'count: ',count

        maxPage = ( count-1 )/eachPageLimit + 1
        print 'maxPage: ',maxPage
        
        eachInfo = eachHouseInfo.objects(**search).skip( skip ).limit( eachPageLimit ) 
        print 'count : ',count
        print ' eachInfo : ',eachInfo
        returnData = {
            'eachInfo':eachInfo,
            'maxPage':maxPage,
            'curPage':pageNum,
            'nextPage':min( maxPage, pageNum + 1 ),
            'prevPage':max( 1, pageNum - 1 ),
            'prices':prices,
            'curLtPrice':intLtPrice,
            'curGtPrice':intGtPrice,
            'apartments':apartments,
            'curApartment': intApartment,
            'sorts':sorts,
            'districts':districts,
            'curDistrict':self.district,
            'curSort':self.sort
        }

        return render( request,'sale.html', returnData )

def dealWithSearch( district,sort,apartment,ltPrice,gtPrice ):
    print 'dealWithSearch ltPrice :',ltPrice
    print 'dealWithSearch gtPrice :',gtPrice
    print ' dealWithSearch apartment :',apartment
    if apartment and int( apartment ) == 0 or not apartment:
        intApartment = 0
        if ltPrice and int( ltPrice ) == 0 or not ltPrice:
            intLtPrice = 0
            intGtPrice = 0
            search =  {
                '__raw__':{
                    'district':{ '$regex': district },
                    'sort': { '$regex': sort }
                }
            }
        else:
            intLtPrice = int( ltPrice )
            intGtPrice = int( gtPrice )
            search =  {
                '__raw__':{
                    'district':{ '$regex': district },
                    'sort': { '$regex': sort },
                    'price':{ '$gte':intGtPrice, '$lte':intLtPrice }
                }
            }
        
    else:
        intApartment = int( apartment )

        if ltPrice and int( ltPrice ) == 0 or not ltPrice:
            intLtPrice = 0
            intGtPrice = 0
            search =  {
                '__raw__':{
                    'district':{ '$regex': district },
                    'room': intApartment ,
                    'sort': { '$regex': sort }
                }
            }
        else:
            intLtPrice = int( ltPrice )
            intGtPrice = int( gtPrice )
            search =  {
                '__raw__':{
                    'district':{ '$regex': district },
                    'sort': { '$regex': sort },
                    'room': intApartment ,
                    'price':{ '$gte':intGtPrice, '$lte':intLtPrice }
                }
            }
        
    return search,intApartment,intLtPrice,intGtPrice
