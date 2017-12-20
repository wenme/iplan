# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from client.models import client, client_action, client_reservation
from insurance.models import product
from common import generate_response, return_code
import datetime
import json
from pyExcelerator import *
from wsgiref.util import FileWrapper
import os

def reserve(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        question = request.POST.get('question', None)
        available_time = request.POST.get('available_time', None)
        ip_addr = request.POST.get('ip_addr', None)
        session_id = request.POST.get('session_id', None)
        client_tag = str(ip_addr) + '_' + str(session_id)

        if name == None or phone == None or available_time == None:
            errmsg = 'params error'
            rslt_json = json.dumps(generate_response.gen('response', {}, return_code.PARAM_ERROR, errmsg))
            response = HttpResponse(rslt_json, content_type='application/json')
            response['Content-Length'] = len(rslt_json)
            return response

        client_reservation_obj = client_reservation.objects.create(
            client_tag = client_tag,
            name = name,
            phone = phone,
            question = question,
            available_time = available_time
        )

        rslt_json = json.dumps(generate_response.gen('response', 'OK', return_code.NORMAL_RESPONSE, None))
        client_action_obj = client_action.objects.create(
            client_tag = client_tag,
            action_name = 'reserve',
            action_post = json.dumps(request.POST),
            action_return = 'OK'
        )
        response = HttpResponse(rslt_json, content_type='application/json')
        response['Content-Length'] = len(rslt_json)
        return response


def get_reservation(request):
    if request.method == 'POST':
        account = request.POST.get('account', None)
        passwd = request.POST.get('password', None)

        if account == None or passwd == None:
            errmsg = 'bad request'
            rslt_json = json.dumps(generate_response.gen('response', {}, return_code.PARAM_ERROR, errmsg))
            response = HttpResponse(rslt_json, content_type='application/json')
            response['Content-Length'] = len(rslt_json)
            return response

        if account != 'iplan' or passwd != 'Bcl12345':
            errmsg = 'bad request'
            rslt_json = json.dumps(generate_response.gen('response', {}, return_code.PARAM_ERROR, errmsg))
            response = HttpResponse(rslt_json, content_type='application/json')
            response['Content-Length'] = len(rslt_json)
            return response

        today = str(datetime.date.today()).replace('-', '_')
        save_file = './client_reservation_files/client_reservation_' + today + '.xls'
        client_reservation_xls = Workbook()
        client_reservation_sheet = client_reservation_xls.add_sheet('client_reservation_sheet')
        row = 0
        col = 0
        count = 0
        print len(client_reservation.objects.all())
        for client_reservation_obj in client_reservation.objects.all():
            client_tag = client_reservation_obj.client_tag
            client_reservation_sheet.write(row, col, u'姓名')
            client_reservation_sheet.write(row, col+2, client_reservation_obj.name)
            client_reservation_sheet.write(row+1, col, u'电话')
            client_reservation_sheet.write(row+1, col+2, client_reservation_obj.phone)
            client_reservation_sheet.write(row+2, col, u'咨询')
            client_reservation_sheet.write(row+2, col+2, client_reservation_obj.question)
            client_reservation_sheet.write(row+3, col, u'可联系时间段')
            client_reservation_sheet.write(row+3, col+2, client_reservation_obj.available_time)
            client_reservation_sheet.write(row+4, col, u'日期')
            client_reservation_sheet.write(row+4, col+2, str(client_reservation_obj.update_date))
            row += 5
            for client_action_obj in client_action.objects.filter(client_tag=client_tag):
                if client_action_obj.action_name == 'get_premium':
                    action_post = json.loads(client_action_obj.action_post)
                    action_return = json.loads(client_action_obj.action_return)                    
                    client_reservation_sheet.write(row, col, u'保险类型')
                    product_type = action_post['product_type']
                    product_type_cn = ''
                    if product_type == 1:
                        product_type_cn = u'意外险'
                    elif product_type == 2:
                        product_type_cn = u'重疾险'
                    elif product_type == 3:
                        product_type_cn = u'综合险'
                    elif product_type == 4:
                        product_type_cn = u'人寿险'
                    elif product_type == 5:
                        product_type_cn = u'医疗险'
                    elif product_type == 6:
                        product_type_cn = u'防癌险'
                    elif product_type == 7:
                        product_type_cn = u'储蓄险'
                    else:
                        product_type_cn = u'无'
                    client_reservation_sheet.write(row+1, col, product_type_cn)
                    client_reservation_sheet.write(row, col+1, u'配置保额')
                    client_reservation_sheet.write(row+1, col+1, action_post['sum_insured'])
                    client_reservation_sheet.write(row, col+2, u'供款年期')
                    client_reservation_sheet.write(row+1, col+2, action_post['premium_period'])
                    client_reservation_sheet.write(row, col+3, u'性别')
                    client_reservation_sheet.write(row+1, col+3, action_post['gender'])
                    client_reservation_sheet.write(row, col+4, u'年龄')
                    client_reservation_sheet.write(row+1, col+4, action_post['application_age'])
                    client_reservation_sheet.write(row, col+5, u'国内')
                    client_reservation_sheet.write(row+1, col+5, action_return['cn_premium'])
                    client_reservation_sheet.write(row, col+6, u'香港')
                    client_reservation_sheet.write(row+1, col+6, action_return['hk_premium'])
                    client_reservation_sheet.write(row, col+7, u'折扣')
                    client_reservation_sheet.write(row+1, col+7, action_return['discount'])
                    col += 8
                elif client_action_obj.action_name == 'product_compare':
                    action_post = json.loads(client_action_obj.action_post)
                    action_return = json.loads(client_action_obj.action_return)
                    print action_post
                    client_reservation_sheet.write(row, col, u'保险比较A')
                    product_a = product.objects.filter(product_code=action_post['product_a'])[0]
                    client_reservation_sheet.write(row+1, col, product_a.product_name)
                    client_reservation_sheet.write(row, col+1, u'保险比较B')
                    product_b = product.objects.filter(product_code=action_post['product_b'])[0]
                    client_reservation_sheet.write(row+1, col+1, product_b.product_name)
                    col += 2
                elif client_action_obj.action_name == 'get_insurance_need':
                    action_post = json.loads(client_action_obj.action_post)
                    action_return = json.loads(client_action_obj.action_return)
                    client_reservation_sheet.write(row, col, u'社保类型')
                    client_reservation_sheet.write(row+1, col, action_post['ans1'])
                    client_reservation_sheet.write(row, col+1, u'收入比重')
                    client_reservation_sheet.write(row+1, col+1, action_post['ans2'])
                    client_reservation_sheet.write(row, col+2, u'剩余按揭')
                    client_reservation_sheet.write(row+1, col+2, action_post['ans3'])
                    client_reservation_sheet.write(row, col+3, u'家庭费用')
                    client_reservation_sheet.write(row+1, col+3, action_post['ans4'])
                    client_reservation_sheet.write(row, col+4, u'是否吸烟')
                    client_reservation_sheet.write(row+1, col+4, action_post['ans5'])
                    client_reservation_sheet.write(row, col+5, u'是否有遗传病')
                    client_reservation_sheet.write(row+1, col+5, action_post['ans6'])
                    client_reservation_sheet.write(row, col+6, u'是否经常出差')
                    client_reservation_sheet.write(row+1, col+6, action_post['ans7'])
                    client_reservation_sheet.write(row, col+7, u'预算')
                    client_reservation_sheet.write(row+1, col+7, action_post['ans8'])
                    client_reservation_sheet.write(row, col+8, u'人寿需求')
                    client_reservation_sheet.write(row+1, col+8, action_return['life_need'])
                    client_reservation_sheet.write(row, col+9, u'重疾需求')
                    client_reservation_sheet.write(row+1, col+9, action_return['critical_illness_need'])
                    client_reservation_sheet.write(row, col+10, u'医疗费用需求')
                    client_reservation_sheet.write(row+1, col+10, action_return['hospital_expense_need'])
                    client_reservation_sheet.write(row, col+11, u'意外保护需求')
                    client_reservation_sheet.write(row+1, col+11, action_return['accidental_protection_need'])
                    client_reservation_sheet.write(row, col+12, u'意外医疗费用需求')
                    client_reservation_sheet.write(row+1, col+12, action_return['accidental_medical_expense_need'])
                    col += 13
                elif client_action_obj.action_name == 'get_education_fee':
                    action_post = json.loads(client_action_obj.action_post)
                    action_return = json.loads(client_action_obj.action_return)
                    client_reservation_sheet.write(row, col, u'学校代码')
                    client_reservation_sheet.write(row+1, col, action_post['university_code'])
                    client_reservation_sheet.write(row, col+1, u'学校名称')
                    client_reservation_sheet.write(row+1, col+1, action_return['name_cn'])
                    client_reservation_sheet.write(row, col+2, u'子女年龄')
                    client_reservation_sheet.write(row+1, col+2, action_post['kid_age'])
                    client_reservation_sheet.write(row, col+3, u'学习类型')
                    client_reservation_sheet.write(row+1, col+3, action_post['scholar_type'])
                    client_reservation_sheet.write(row, col+4, u'预计通胀率')
                    client_reservation_sheet.write(row+1, col+4, action_post['expected_inflation'])
                    client_reservation_sheet.write(row, col+5, u'预计回报率')
                    client_reservation_sheet.write(row+1, col+5, action_post['expected_return_rate'])
                    client_reservation_sheet.write(row, col+6, u'每年费用')
                    client_reservation_sheet.write(row+1, col+6, action_return['yearly_cost'])
                    client_reservation_sheet.write(row, col+7, u'总费用')
                    client_reservation_sheet.write(row+1, col+7, action_return['total_cost'])
                    client_reservation_sheet.write(row, col+8, u'距今多少年')
                    client_reservation_sheet.write(row+1, col+8, action_return['year_to_come'])
                    client_reservation_sheet.write(row, col+9, u'目标金额')
                    client_reservation_sheet.write(row+1, col+9, action_return['target_saving'])
                    client_reservation_sheet.write(row, col+10, u'每月储蓄')
                    client_reservation_sheet.write(row+1, col+10, action_return['monthly_saving'])
                    col += 11
            
            row += 3
            col = 0
            count += 1

        client_reservation_xls.save(save_file)
        wrapper = FileWrapper(file(save_file))
        response = HttpResponse(wrapper, content_type='application/octet-stream')
        response['Content-Length'] = os.path.getsize(save_file)
        response['Content-Disposition'] = 'attachment; filename=%s' % ('client_reservation_' + today + '.xls')
        return response
