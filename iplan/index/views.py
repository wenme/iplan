# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse

def home_page(request):
    rslt = get_template('demo_home_page.html')
    html = rslt.render()
    return HttpResponse(html)

def get_insurance_need(request):
    rslt = get_template('insurance_need.html')
    html = rslt.render()
    return HttpResponse(html)

def get_education_fund(request):
    rslt = get_template('education_fund.html')
    html = rslt.render()
    return HttpResponse(html)

def product_cmp(request):
    rslt = get_template('product_cmp.html')
    html = rslt.render()
    return HttpResponse(html)

def get_insurance_fee(request):
    rslt = get_template('insurance_fee.html')
    html = rslt.render()
    return HttpResponse(html)

def get_retirement_fund(request):
    rslt = get_template('retirement_fund.html')
    html = rslt.render()
    return HttpResponse(html)

