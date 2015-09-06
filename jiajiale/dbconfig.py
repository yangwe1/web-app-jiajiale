# -*- coding=utf-8 -*-
# Created Time: Wed 20 Aug 2014 02:51:13 PM CST
# File Name: dbconfig.py
import hashlib
import pymongo
import types
import json
import random
from datetime import datetime
# from func import weibo_txt,weibo_uinfo,tb_content
# from dbhbase import get_shop_info
host = '127.0.0.1'
port = 27017

conn = pymongo.Connection(host, port)
jiajiale = conn['jiajiale']
rentInfo = jiajiale['rentInfo']
# tb_user = wtq['tb_user']

Property  = ["酒厂南苑","电子科大清水河","电子科大沙河","顺江小区","龙湖时代天街","龙湖三千集","财富又一城","锦江宾馆","四川大学"]
address = ["成都市高新西区西源大道2006号","成都市高新区IT大道2006号","成都市金牛水池额大道2006号","成都市锦江区银杏大道006号","成都市成华区成华大道26号","成都市龙泉驿区新抚大道008号","成都市郫县源大道239号","成都市青羊区瞎学大道2006号","成都市双流县大道379号","成都市高新区低级黑大道2006号",]
district = ["市区","郊区","开发区","博昌","锦秋","湖滨","店子","兴福","曹王","陈户","吕艺","庞家","纯化","乔庄","其他"]
sort = ["新房","二手房","办公写字楼","店面商铺","平房/独院/地皮","厂房/仓库/车库","别墅","其他房讯"]
remark = [
    "带有车库，证已出五年，过户费低。　联系我时请说明是在博兴在线看到的……",
    "有储藏室，学校附近，交通方便，人文环境好。　联系我时请说明是在博兴在线看到的……",
    "双证，储藏室。新世纪东临。　联系我时请说明是在博兴在线看到的……",
    "有储藏室。。。　联系我时请说明是在博兴在线看到的……"
]
apartment = [
    "复式",
    "一室一厅",
    "两室一厅",
    "两室两厅",
    "三室一厅",
    "三室两厅",
    "四室",
    "单间/开间",
]

def insertInfo(): 
    eachProperty = random.sample(Property,1)[0]
    eachAddress = random.sample(address,1)[0]
    eachDistrict = random.sample(district,1)[0]
    eachSort = random.sample(sort,1)[0]
    eachRemark = random.sample(remark,1)[0]
    eachApartment = random.sample( apartment, 1 )[0]

    # date = [str(random.randint(1990,2014)),'/',str(random.randint(1,12)),'/',str(random.randint(1,30)),'/',' ',str(random.randint(1,24)),':',str(random.randint(00,59))]
    # eachDate = ''
    # eachDate = ''.join(date)
    # print 'eachDate : ',eachDate

    eachInfo = {
        "houseID":random.randint(1,2000),
        "eachProperty":eachProperty,### 楼盘 ####
        "phone":18583607687,
        # "building":random.randint(2,39899), ### 
        "unit":random.randrange(1,100), ### 单元号 ###
        "doorNum":random.randint(100,10000), ##### 房间号 #####
        "house_age":random.randint(1990,2014), ### 房龄 ###
        "floor":random.randint(1,50),#### 楼层 #####
        "floorCount":random.randint(1,100), ##### 楼层总数 #######
        "room":random.randint(1,5), 
        "hall":random.randint(1,2), ### 厅 ###
        "area":random.randint(50,200), ### 面积 ###
        "price":random.randint(200,20000), ### 价格 ### 
        "keyNum":random.randint(100,10000), ### 钥匙编号 ###
        "remark":eachRemark, ### 备注 ###
        "address":eachAddress, ### 详细地址 ###
        "tag" :random.randint(100,10000), ### 标签 ### 
        "date":datetime.now(), ### 创建时间 ###
        #"eachSqurePrice":random.randint(2000,19000), ### 每平方米价格 ###
        "district":eachDistrict, ### 小区 ###
        "sort":eachSort ### 分类 ###
    }

    rentInfo.insert(eachInfo)
    # print ' eachInfo : ',eachInfo

def eachInsert():
    count = 0
    while (count < 3000):
        insertInfo()
        count = count + 1

if __name__ == '__main__':
    eachInsert() 











