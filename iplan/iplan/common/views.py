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
