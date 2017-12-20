# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
import generate_response, return_code
import json

def err_404(request):
    errmsg = 'page not found'
    rslt_json = json.dumps(generate_response.gen('response', {}, return_code.PAGE_NOT_FOUND, errmsg))
    response = HttpResponse(rslt_json, content_type='application/json')
    response['Content-Length'] = len(rslt_json)
    return response

def err_500(request):
    errmsg = 'internal error'
    rslt_json = json.dumps(generate_response.gen('response', {}, return_code.INTERNAL_ERROR, errmsg))
    response = HttpResponse(rslt_json, content_type='application/json')
    response['Content-Length'] = len(rslt_json)
    return response

def error_detect(request):
    if request.method == "POST":
        account = request.POST.get('account', None)
        passwd = request.POST.get('passwd', None)
        
        if account == None or passwd == None or ( account != 'ck' or passwd != '332465723'):
            errmsg = 'internal error'
            rslt_json = json.dumps(generate_response.gen('response', 0, return_code.INTERNAL_ERROR, errmsg))
            response = HttpResponse(rslt_json, content_type='application/json')
            response['Content-Length'] = len(rslt_json)
            return response

        rslt_json = json.dumps(generate_response.gen('response', 1, return_code.NORMAL_RESPONSE, None))
        response = HttpResponse(rslt_json, content_type='application/json')
        response['Content-Length'] = len(rslt_json)
        return response
        
