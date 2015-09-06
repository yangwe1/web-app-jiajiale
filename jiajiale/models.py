# -*- coding=utf-8 -*-

from mongoengine import *
# from mongoengine.django.auth import User
from datetime import datetime

class eachHouseInfo(Document):
    """每个房源的详细信息"""

    houseID = IntField()
    eachID = ObjectIdField()
    eachProperty = StringField(default='')
    phone = IntField()
    buidling = IntField()
    unit = IntField()
    doorNum = IntField()
    house_age = IntField()
    floor = IntField()
    floorCount = IntField()
    room = IntField()
    hall = IntField()
    area = IntField()
    price = IntField()
    keyNum = IntField()
    remark = StringField(default='')
    address = StringField(default='')
    tag = IntField()
    #date = DateTimeField(default=datetime.now)
    saleStyle = StringField(default='')
    eachSqurePrice = IntField()
    district = StringField(default="")
    sort = StringField(default="")
    #imgUrl = ListField(ObjectIdField())

    meta = {
        'collection':'info'
    }

class eachRentInfo(Document):
    """每个房源的详细信息"""

    houseID = IntField()
    eachProperty = StringField(default='')
    phone = StringField()
    buidling = IntField()
    unit = StringField()
    doorNum = StringField()
    house_age = IntField()
    floor = StringField()
    floorCount = StringField()
    room = StringField()
    hall = StringField()
    area = IntField()
    price = IntField()
    keyNum = IntField()
    remark = StringField(default='')
    address = StringField(default='')
    tag = IntField()
    #date = DateTimeField(default=datetime.now)
    eachSqurePrice = IntField()
    district = StringField(default="")
    sort = StringField(default="")
    #imgUrl = ListField(ObjectIdField())

    meta = {
        'collection':'rentInfo'
    }
