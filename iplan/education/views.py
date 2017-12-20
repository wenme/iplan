# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import university, university_fee, university_ranking
from common import oss_handler, generate_response, return_code
from client.models import client_action
from insurance.models import insurer, product
import datetime
import json
import math

def total_cost_with_inflation(total_cost, year_to_come, expected_inflation):
    return int( float(total_cost) * (float(1+expected_inflation)**year_to_come) )

def monthly_saving(targer_saving, year_to_come, expected_return_rate):
    return int( float(targer_saving) * expected_return_rate / ((1+expected_return_rate)**year_to_come - 1) / 12 )

def filter_university(request):
    if request.method == 'POST':
        region = request.POST.get('region', None)
        expert = request.POST.get('expert', 'qs_ranking')
        yearly_cost = int(request.POST.get('yearly_cost', 99999999))
        page = int(request.POST.get('page', 0))
        ip_addr = request.POST.get('ip_addr', None)
        session_id = request.POST.get('session_id', None)
        client_tag = str(ip_addr) + '_' + str(session_id)
        expert_condition = {}
        expert_condition[expert+'__gte'] = 1

        university_list = []
        this_year = str(datetime.datetime.now().year) + '-1-1'
        # print len(university_ranking.objects.filter(year__gte=this_year).order_by(expert))
        for ur_obj in university_ranking.objects.filter(year__gte=this_year).filter(**expert_condition).order_by(expert):
            uf_obj = university_fee.objects.filter(university_code=ur_obj.university_code, year__gte=this_year)[0]
            u_obj = university.objects.filter(university_code=ur_obj.university_code)[0]
            u_obj_json = {}
            if uf_obj.cost <= yearly_cost and ( region == None or region == ''):
                u_obj_json['university_code'] = ur_obj.university_code
                u_obj_json['university_ranking'] = ur_obj.qs_ranking
                u_obj_json['university_name'] = u_obj.name_cn
                university_list.append(u_obj_json)
            elif uf_obj.cost <= yearly_cost and u_obj.region == region:
                u_obj_json['university_code'] = ur_obj.university_code
                u_obj_json['university_ranking'] = ur_obj.qs_ranking
                u_obj_json['university_name'] = u_obj.name_cn
                university_list.append(u_obj_json)
            else:
                print 'ha? university_code:', ur_obj.university_code

        sub_university_list_json = {}
        if page != 0:
            page = page - 1
        sub_university_list_json['sub_list'] = university_list[page*5:page*5+5]
        sub_university_list_json['total_count'] = len(university_list)
        rslt_json = json.dumps(generate_response.gen('sub_university_list', sub_university_list_json, return_code.NORMAL_RESPONSE, None))
        client_action_obj = client_action.objects.create(
            client_tag = client_tag,
            action_name = 'filter_university',
            action_post = json.dumps(request.POST),
            action_return = json.dumps(sub_university_list_json)
        )
        response = HttpResponse(rslt_json, content_type='application/json')
        response['Content-Length'] = len(rslt_json)
        return response


def get_university_info(request):
    if request.method == 'POST':
        university_code = request.POST.get('university_code', None)
        ip_addr = request.POST.get('ip_addr', None)
        session_id = request.POST.get('session_id', None)
        client_tag = str(ip_addr) + '_' + str(session_id)

        if university_code == None:
            errmsg = 'params error'
            rslt_json = json.dumps(generate_response.gen('response', {}, return_code.PARAM_ERROR, errmsg))
            response = HttpResponse(rslt_json, content_type='application/json')
            response['Content-Length'] = len(rslt_json)
            return response

        u_obj = university.objects.filter(university_code=university_code)[0]
        this_year = str(datetime.datetime.now().year) + '-1-1'
        ur_obj = university_ranking.objects.filter(university_code=university_code, year__gte=this_year)[0]
        uf_obj = university_fee.objects.filter(university_code=university_code, year__gte=this_year)[0]
        university_info_json = {}
        university_info_json['name_cn'] = u_obj.name_cn
        university_info_json['name_en'] = u_obj.name_en
        university_info_json['qs_ranking'] = ur_obj.qs_ranking
        university_info_json['cost'] = uf_obj.cost
        university_info_json['country'] = u_obj.country
        university_info_json['website'] = u_obj.website
        university_info_json['introduction'] = u_obj.introduction
        university_info_json['logo'] = u_obj.logo
        university_info_json['pic1'] = u_obj.pic1
        university_info_json['pic2'] = u_obj.pic2
        university_info_json['pic3'] = u_obj.pic3
        rslt_json = json.dumps(generate_response.gen('university_info', university_info_json, return_code.NORMAL_RESPONSE, None))
        client_action_obj = client_action.objects.create(
            client_tag = client_tag,
            action_name = 'get_university_info',
            action_post = json.dumps(request.POST),
            action_return = json.dumps(university_info_json)
        )
        response = HttpResponse(rslt_json, content_type='application/json')
        response['Content-Length'] = len(rslt_json)
        return response


def get_education_fee(request):
    if request.method == 'POST':
        university_code = request.POST.get('university_code', None)
        kid_age = request.POST.get('kid_age', None)
        scholar_type = int(request.POST.get('scholar_type', None))
        expected_inflation = request.POST.get('expected_inflation', None)
        expected_return_rate = request.POST.get('expected_return_rate', None)
        ip_addr = request.POST.get('ip_addr', None)
        session_id = request.POST.get('session_id', None)
        client_tag = str(ip_addr) + '_' + str(session_id)
        
        if university_code == None or kid_age == None or scholar_type == None or expected_inflation == None or expected_return_rate == None:
            errmsg = 'params error'
            rslt_json = json.dumps(generate_response.gen('response', {}, return_code.PARAM_ERROR, errmsg))
            response = HttpResponse(rslt_json, content_type='application/json')
            response['Content-Length'] = len(rslt_json)
            return response

        expected_inflation = float(expected_inflation) / 100.0
        expected_return_rate = float(expected_return_rate) / 100.0
        school_year = 0
        school_age = 0
        if scholar_type == 1:
            school_year = 4
            school_age = 18
        elif scholar_type == 2:
            school_year = 2
            school_age = 22
        elif scholar_type == 3:
            school_year = 6
            school_age = 18
        else:
            errmsg = 'sholar type error'
            rslt_json = json.dumps(generate_response.gen('response', {}, return_code.PARAM_ERROR, errmsg))
            response = HttpResponse(rslt_json, content_type='application/json')
            response['Content-Length'] = len(rslt_json)
            return response

        education_fee_info_json = {}
        this_year = str(datetime.datetime.now().year) + '-1-1'
        u_obj = university.objects.filter(university_code=university_code)[0]
        uf_obj = university_fee.objects.filter(university_code=university_code, year__gte=this_year)[0]
        education_fee_info_json['name_cn'] = u_obj.name_cn
        education_fee_info_json['yearly_cost'] = uf_obj.cost
        education_fee_info_json['total_cost'] = uf_obj.cost * school_year
        education_fee_info_json['year_to_come'] = school_age - int(kid_age)
        education_fee_info_json['target_saving'] = total_cost_with_inflation(education_fee_info_json['total_cost'], education_fee_info_json['year_to_come'], expected_inflation) 
        education_fee_info_json['monthly_saving'] = monthly_saving(education_fee_info_json['target_saving'], education_fee_info_json['year_to_come'], expected_return_rate)
        
        # product recommendation of PU NENG
        recommend_product_list = []
        recommend_product_code_list = [134,31,34]
        for product_obj in product.objects.filter(product_code__in=recommend_product_code_list):
            product_info_tmp = {}
            product_info_tmp['product_name'] = product_obj.product_name
            product_info_tmp['application_age_min'] = product_obj.application_age_min
            product_info_tmp['application_age_max'] = product_obj.application_age_max
            product_info_tmp['benefit_age_max'] = product_obj.benefit_age_max if product_obj.benefit_age_max < 100 else '终身'
            product_type_tmp = product_obj.product_type
            if product_type_tmp == 2:
                product_info_tmp['product_type'] = '重疾险'
            if product_type_tmp == 4:
                product_info_tmp['product_type'] = '人寿险'
            insurer_code_tmp = product_obj.insurer_code
            insurer_obj_tmp = insurer.objects.get(insurer_code=insurer_code_tmp)
            product_info_tmp['insurer_name'] = insurer_obj_tmp.insurer_name
            recommend_product_list.append(product_info_tmp)
        education_fee_info_json['recommend_product_list'] = recommend_product_list
        # end of product recommendation of PU NENG

        rslt_json = json.dumps(generate_response.gen('education_fee_info', education_fee_info_json, return_code.NORMAL_RESPONSE, None))
        client_action_obj = client_action.objects.create(
            client_tag = client_tag,
            action_name = 'get_education_fee',
            action_post = json.dumps(request.POST),
            action_return = json.dumps(education_fee_info_json)
        )
        response = HttpResponse(rslt_json, content_type='application/json')
        response['Content-Length'] = len(rslt_json)
        return response
