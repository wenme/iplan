# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
import views

urlpatterns = [
    url(r'^get_premium/$', views.get_premium, name="get_premium"),
    url(r'^get_insurance_list/$', views.get_insurance_list, name="get_insurance_list"),
    url(r'^product_compare/$', views.product_compare, name="product_compare"),
    url(r'^get_insurance_need', views.get_insurance_need, name="get_insurance_need"),
]
