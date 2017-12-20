# -*- coding: utf-8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^filter_university/$', views.filter_university, name="filter_university"),
    url(r'^get_university_info/$', views.get_university_info, name="get_university_info"),
    url(r'^get_education_fee/$', views.get_education_fee, name="get_education_fee"),
]
