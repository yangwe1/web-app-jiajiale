# -*- coding=utf-8 -*-
# author guiche
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import HttpResponse, redirect, render
from django.shortcuts import render_to_response
#from django.template import Template

from models import eachRentInfo 

class getRentList( View ):

    context_object_name = 'eachInfo'
    template_name = 'rent.html'

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
            {'gtPrice':0,  'ltPrice':300,'name':u"300以下"},
            {'gtPrice':300, 'ltPrice':500,'name':u"300元-500元"},
            {'gtPrice':500, 'ltPrice':800,'name':u"500元-800元"},
            {'gtPrice':800, 'ltPrice':1000,'name':u"800元-1000元"},
            {'gtPrice':1000, 'ltPrice':1500,'name':u"1000元-1500元"},
            {'gtPrice':1500, 'ltPrice':2000,'name':u"1500元-2000元"},
            {'gtPrice':2000, 'ltPrice':2500,'name':u"2000元-2500元"},
            {'gtPrice':2500, 'ltPrice':3000,'name':u"2500元-3000元"},
            {'gtPrice':3000,'ltPrice':5000,'name':u"3000元-5000元"},
            {'gtPrice':5000,'ltPrice':10000,'name':u"5000元-10000元"},
            {'gtPrice':10000,'ltPrice':50000,'name':u"10000元以上"},
        ]
        
        search,intApartment,intLtPrice,intGtPrice = dealWithSearch( self.district,self.sort,self.apartment,self.ltPrice,self.gtPrice )

        print 'search: ',search
        pageNum = 1 
        if self.page and self.page.isalnum(): 
            pageNum = max( 1, int(self.page) )
        print 'pageNum: ',pageNum
        eachPageLimit = 24 
        skip = ( pageNum -1 ) * eachPageLimit
        count = eachRentInfo.objects( **search ).count()
        print 'count: ',count

        maxPage = ( count-1 )/eachPageLimit + 1
        print 'maxPage: ',maxPage
        
        eachInfo = eachRentInfo.objects(**search).skip( skip ).limit( eachPageLimit ) 
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

        return render( request,'rent.html', returnData )

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
