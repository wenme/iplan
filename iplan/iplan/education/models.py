# -*- coding: utf-8 -*-

from django.db import models
import django.utils.timezone

class university(models.Model):
    university_code = models.CharField('id', primary_key=True, max_length=20)
    name_cn = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    fee_page = models.TextField(default='', null=True)
    website = models.TextField(default='', null=True)
    introduction = models.TextField(default='', null=True)
    logo = models.TextField(default='', null=True)
    pic1 = models.TextField(default='', null=True)
    pic2 = models.TextField(default='', null=True)
    pic3 = models.TextField(default='', null=True)

class university_fee(models.Model):
    id =  models.AutoField('id', primary_key=True)
    university_code = models.CharField(max_length=20)
    year = models.DateTimeField(null=True)
    currency = models.CharField(max_length=50)
    tuition = models.FloatField(null=True)
    live_expense = models.FloatField(null=True)
    local_cost = models.FloatField(null=True)
    exchange_rate = models.FloatField(null=True)
    cost = models.FloatField(null=True)

class university_ranking(models.Model):
    id =  models.AutoField('id', primary_key=True)
    year = models.DateTimeField(null=True)
    qs_ranking = models.IntegerField(null=True)
    university_code = models.CharField(max_length=20)
    arts_humanities = models.IntegerField(null=True)
    engineering_technology = models.IntegerField(null=True)
    life_sciences_medicine = models.IntegerField(null=True)
    natural_science = models.IntegerField(null=True)
    social_sciences_management = models.IntegerField(null=True)
    
