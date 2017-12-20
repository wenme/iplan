# -*- coding: utf-8 -*-

from django.db import models
import django.utils.timezone

class client(models.Model):
    GERNDER_TYPE = (
        (0, 'female'),
        (1, 'male')
    )
    client_id = models.AutoField('id', primary_key=True)
    account = models.CharField(max_length=64, unique=True, default="")
    name = models.CharField(max_length=64, default="")
    age = models.IntegerField()
    gender = models.IntegerField(choices=GERNDER_TYPE)
    phone = models.CharField(max_length=64, unique=True, null=True)
    email = models.CharField(max_length=64, unique=True, null=True)
    password = models.CharField(max_length=64, default="")
    register_date = models.DateTimeField(default=django.utils.timezone.now)
    client_tag = models.CharField(max_length=64, null=True)

class client_action(models.Model):
    id = models.AutoField('id', primary_key=True)
    client_tag = models.CharField(max_length=64, null=True)
    action_name = models.CharField(max_length=64, null=True)
    action_post = models.TextField(null=True)
    action_return = models.TextField(null=True)
    update_date = models.DateTimeField(default=django.utils.timezone.now)
    
class client_reservation(models.Model):
    id = models.AutoField('id', primary_key=True)
    client_tag = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=64, default="")
    phone = models.CharField(max_length=64, null=True)
    question = models.TextField(null=True)
    available_time = models.CharField(max_length=64, null=True)
    update_date = models.DateTimeField(default=django.utils.timezone.now)
   
