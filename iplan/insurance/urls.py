# -*- coding: utf-8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^get_premium/$', views.get_premium, name="get_premium"),
    url(r'^get_premium_rate/$', views.get_premium_rate, name="get_premium_rate"),
    url(r'^get_premium_rate_range/$', views.get_premium_rate_range, name="get_premium_rate_range"),
    url(r'^get_insurance_list/$', views.get_insurance_list, name="get_insurance_list"),
    url(r'^product_compare/$', views.product_compare, name="product_compare"),
    url(r'^get_insurance_need', views.get_insurance_need, name="get_insurance_need"),
    url(r'^super_find/$', views.admin_find, name="admin_find"),
    url(r'^super_modify/$', views.admin_modify, name="admin_modify"),
]
