# -*- coding: utf-8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^demo', views.home_page, name="home_page"),
    url(r'^insurance_need', views.get_insurance_need, name="get_insurance_need"),
    url(r'^education_fund', views.get_education_fund, name="get_education_fund"),
    url(r'^product_cmp', views.product_cmp, name="product_cmp"),
    url(r'^insurance_fee', views.get_insurance_fee, name="get_insurance_fee"),
    url(r'^retirement_fund', views.get_retirement_fund, name="get_retirement_fund"),
]
