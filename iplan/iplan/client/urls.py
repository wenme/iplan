# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
import views

urlpatterns = [
    url(r'^reserve/$', views.reserve, name="reserve"),
    url(r'^get_reservation/$', views.get_reservation, name="get_reservation"),
]

