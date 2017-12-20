# -*- coding: utf-8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^retire_fee/$', views.retire_fee, name="retire_fee"),
]
