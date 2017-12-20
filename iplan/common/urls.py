# -*- coding: utf-8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^error_detect/$', views.error_detect, name="error_detect"),
]

