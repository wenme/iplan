# -*- coding: utf-8 -*-

from django.db import models
import django.utils.timezone

class questionaire_ans(models.Model):
    SOCIAL_SECURITY_TYPE1 = 1
    SOCIAL_SECURITY_TYPE2 = 2
    SOCIAL_SECURITY_TYPE3 = 3
    SOCIAL_SECURITY_TYPE_CHOICES = (
        (SOCIAL_SECURITY_TYPE1, 'medical_insurance'),
        (SOCIAL_SECURITY_TYPE2, 'free_medical_service'),
        (SOCIAL_SECURITY_TYPE3, 'none'),
    )
    client_id = models.IntegerField('id', primary_key=True)
    social_security = models.IntegerField(choices=SOCIAL_SECURITY_TYPE_CHOICES)
    income_weight = models.FloatField()
    mortgage_balance = models.IntegerField()
    household_expense = models.IntegerField()
    smoking = models.BooleanField()
    inheritance = models.BooleanField()
    trip_frequency = models.BooleanField()
    budget = models.IntegerField()
    update_date = models.DateTimeField(default=django.utils.timezone.now)

class need(models.Model):
    client_id = models.IntegerField('id', primary_key=True)
    life_need = models.IntegerField()
    critical_illness_need = models.IntegerField()
    hospital_expense_need = models.IntegerField()
    accidental_protection_need = models.IntegerField()
    accidental_medical_expense_need = models.IntegerField()

class feedback(models.Model):
    client_id = models.IntegerField('id', primary_key=True)
    score = models.IntegerField()
    redeem = models.BooleanField()
    update_date = models.DateTimeField(default=django.utils.timezone.now)

class need_analysis(models.Model):
    client_id = models.IntegerField('id', primary_key=True)
    death_illness = models.IntegerField()
    ci_illness = models.IntegerField()
    hospital_illness = models.IntegerField()
    disable_illness = models.IntegerField()
    death_accident = models.IntegerField()
    ci_accident = models.IntegerField()
    hospital_accident = models.IntegerField()
    disable_accident = models.IntegerField()

class plan(models.Model):
    client_id = models.IntegerField('id', primary_key=True)
    protection_score = models.IntegerField()
    life = models.IntegerField()
    critical_illness = models.IntegerField()
    hospital_expense = models.IntegerField()
    accidental_protection = models.IntegerField()
    accidental_medical_expense = models.IntegerField()
    total_fyp = models.FloatField()
    avg_premium = models.FloatField(null=True)
    irr = models.FloatField(null=True)
    loading = models.FloatField()

class advice(models.Model):
    id =  models.AutoField('id', primary_key=True)
    client_id = models.IntegerField()
    product_name = models.CharField(max_length=64)
    insurer = models.CharField(max_length=64)
    product_type = models.IntegerField()
    annual_premium = models.FloatField()
    avg_premium = models.FloatField(null=True)
    premium_period = models.IntegerField()
    benefit_age_max = models.IntegerField()
    life = models.IntegerField()
    critical_illness = models.IntegerField()
    hospital_expense = models.IntegerField()
    accidental_protection = models.IntegerField()
    accidental_medical_expense = models.IntegerField()
    saving = models.BooleanField()
    product_logo = models.CharField(max_length=32)
    product_url = models.TextField()

class rule(models.Model):
    protection_id = models.IntegerField('id', primary_key=True)
    protection_name = models.CharField(max_length=32)
    priority = models.FloatField()
    benchmark = models.IntegerField()
    non_social_security = models.IntegerField()
    gov_medical_care = models.IntegerField()
    smoker = models.IntegerField()
    hereditary_disease = models.IntegerField()
    traveller = models.IntegerField()
    benefit_age_min = models.IntegerField()

class insurer(models.Model):
    insurer_code = models.CharField('id', primary_key=True, max_length=20)
    insurer_name = models.CharField(max_length=100)
    region = models.CharField(max_length=20)
    logo = models.TextField()

class product(models.Model):
    # PRODUCT_TYPE
    PRODUCT_TYPE_ACCIDENT = 1
    PRODUCT_TYPE_CRITICAL_ILLNESS = 2
    PRODUCT_TYPE_COMPREHENSIVE = 3
    PRODUCT_TYPE_LIFE = 4
    PRODUCT_TYPE_MEDICAL = 5
    PRODUCT_TYPE_CANCER = 6
    PRODUCT_TYPE_SAVING = 7
    PRODUCT_TYPE_CHOICES = (
        (PRODUCT_TYPE_ACCIDENT, 'accident_insurance'),
        (PRODUCT_TYPE_CRITICAL_ILLNESS, 'critical_illness_insurance'),
        (PRODUCT_TYPE_COMPREHENSIVE, 'comprehensive_insurance'),
        (PRODUCT_TYPE_LIFE, 'life_insurance'),
        (PRODUCT_TYPE_MEDICAL, 'medical_insurance'),
        (PRODUCT_TYPE_CANCER, 'cancer_insurance'),
        (PRODUCT_TYPE_SAVING, 'saving_insurance'),
    )
    # CHANNEL_TYPE
    CHANNEL_TYPE_OFFLINE = 0
    CHANNEL_TYPE_ONLINE = 1
    CHANNEL_TYPE_AGENT = 2
    CHANNEL_TYPE_CHOICES = (
        (CHANNEL_TYPE_OFFLINE, 'offline'),
        (CHANNEL_TYPE_ONLINE, 'online'),
        (CHANNEL_TYPE_AGENT, 'agent'),
    )
    # PRICE_TABLE
    TABLE_NONE = 0
    TABLE_QUOTATION = 1
    TABLE_PREMIUM_RATE = 2
    TABLE_CHOICES = (
        (TABLE_NONE, 'no price'),
        (TABLE_QUOTATION, 'quotation'),
        (TABLE_PREMIUM_RATE, 'premium_rate'),
    )
    product_code = models.IntegerField('id', primary_key=True)
    internal_code = models.CharField(max_length=64)
    product_name = models.CharField(max_length=100)
    insurer_code = models.CharField(max_length=64)
    launch_year = models.DateTimeField(null=True)
    application_age_min = models.IntegerField(null=True)
    application_age_max = models.IntegerField(null=True)
    benefit_age_max = models.IntegerField(null=True)
    min_face_amount = models.IntegerField(null=True)
    max_face_amount = models.IntegerField(null=True)
    product_type = models.IntegerField(choices=PRODUCT_TYPE_CHOICES,null=True)
    channel = models.IntegerField(choices=CHANNEL_TYPE_CHOICES,null=True)
    long_term = models.NullBooleanField(null=True)
    currency = models.CharField(max_length=20,null=True)
    rider = models.NullBooleanField(null=True)
    life = models.NullBooleanField(null=True)
    ci = models.NullBooleanField(null=True)
    ap = models.NullBooleanField(null=True)
    med = models.NullBooleanField(null=True)
    saving = models.NullBooleanField(null=True)
    investment = models.NullBooleanField(null=True)
    price_table = models.IntegerField(choices=TABLE_CHOICES,null=True)
    terms = models.TextField(null=True)
    brochure = models.TextField(null=True)
    product_url = models.TextField(null=True)
    cover_url = models.TextField(null=True)

class product_feature(models.Model):
    product_code = models.IntegerField('id', primary_key=True)
    average_loading = models.FloatField()
    median_loading = models.FloatField()
    core_benefit_amount = models.IntegerField()
    critical_illness_life = models.BooleanField()
    life_min = models.IntegerField()
    life_max = models.IntegerField()
    critical_illness_min = models.IntegerField()
    critical_illness_max = models.IntegerField()
    hospital_expense_min = models.IntegerField()
    hospital_expense_max = models.IntegerField()
    accident_protect_min = models.IntegerField()
    accident_protect_max = models.IntegerField()
    accident_medical_expense_min = models.IntegerField()
    accident_medical_expense_max = models.IntegerField()
    maturity_min = models.IntegerField()
    maturity_max = models.IntegerField()

class life(models.Model):
    # CLAIM_18_TYPE
    NO_CONSTRAINT = 0
    LT_10W_BEFORE_18 = 1
    RETURN_PREMIUM_BEFORE_18 =2
    CLAIM_18_TYPE_CHOICES = (
        (NO_CONSTRAINT, 'no_constraints'),
        (LT_10W_BEFORE_18, 'less_than_million_before_18'),
        (RETURN_PREMIUM_BEFORE_18, 'return_premium_before_18'),
    )
    # CLAIM_BASE_TYPE
    SUM_ASSURED = 1
    PREMIUM = 2
    CLAIM_BASE_TYPE_CHOICES = (
        (SUM_ASSURED, 'sum_assured'),
        (PREMIUM, 'premium'),
    )
    product_code = models.IntegerField('id', primary_key=True)
    waiting_period = models.IntegerField(null=True)
    claim_18 = models.IntegerField(choices=CLAIM_18_TYPE_CHOICES, null=True)
    claim_base = models.IntegerField(choices=CLAIM_BASE_TYPE_CHOICES, null=True)
    death_illness = models.FloatField(null=True)
    death_accident = models.FloatField(null=True)
    advance_payment_with_ci = models.NullBooleanField(null=True)
    permanent_disability = models.NullBooleanField(null=True)
    face_amount_growth_rate = models.FloatField(null=True)

class ci(models.Model):
    # non_ci_claim_method
    NO_CLAIM = 0
    COME_WITH_CI = 1
    EXTRA_CLAIM = 2
    NON_CI_CLAIM_CHOICES = (
        (NO_CLAIM, 'no_claim'),
        (COME_WITH_CI, 'come_with_ci'),
        (EXTRA_CLAIM, 'extra_cliam'),
    )
    product_code = models.IntegerField('id', primary_key=True)
    waiting_period = models.IntegerField(null=True)
    ci = models.IntegerField(null=True)
    ci_max_claim =  models.IntegerField(null=True)
    non_ci = models.IntegerField(null=True)
    non_ci_max_claim = models.IntegerField(null=True)
    non_ci_claim_method = models.IntegerField(choices=NON_CI_CLAIM_CHOICES, null=True)
    early_stage_ci = models.IntegerField(null=True)
    early_stage_ci_claim = models.FloatField(null=True)
    juvenile_minor_illness = models.IntegerField(null=True)
    cancer_max_claim = models.IntegerField(null=True)
    cancer_total_claim = models.IntegerField(null=True)
    face_amount_growth_rate = models.FloatField(null=True)
    waiver = models.NullBooleanField(null=True)
    first_n_year_plus = models.FloatField(null=True)
    first_n_year = models.IntegerField(null=True)

class saving(models.Model):
    # PAR_TYPE
    NO_PAR = 0
    AMERICAN_PAR = 1
    BRITISH_PAR = 2
    CASH_PAR = 3
    PAR_TYPE_CHOICES = (
        (NO_PAR, 'no_par'),
        (AMERICAN_PAR, 'american_par'),
        (BRITISH_PAR, 'british_par'),
        (CASH_PAR, 'cash_par'),
    )
    product_code = models.IntegerField('id', primary_key=True)
    y40_guaranteed_irr = models.FloatField(null=True)
    y10_expected_irr = models.FloatField(null=True)
    y20_expected_irr = models.FloatField(null=True)
    y30_expected_irr = models.FloatField(null=True)
    y40_expected_irr = models.FloatField(null=True)
    y50_expected_irr = models.FloatField(null=True)
    maturity_expected_irr = models.FloatField(null=True)
    par = models.IntegerField(choices=PAR_TYPE_CHOICES, null=True)
    par_distribution = models.FloatField(null=True)
    annuity = models.NullBooleanField(null=True)
    bonus_encash_year = models.IntegerField(null=True)
    surrender_partially_year = models.IntegerField(null=True)
    site_url = models.TextField(null=True)
    y10_guaranteed_irr = models.FloatField(null=True)
    y20_guaranteed_irr = models.FloatField(null=True)
    y30_guaranteed_irr = models.FloatField(null=True)
    y50_guaranteed_irr = models.FloatField(null=True)
    maturity_guaranteed_irr = models.FloatField(null=True)
    longevity = models.NullBooleanField(null=True)
    guaranteed_payback_period = models.IntegerField(null=True)
    expected_payback_period = models.IntegerField(null=True)

class quotation(models.Model):
    GENDER_TYPE_FEMALE = 0
    GENDER_TYPE_MALE = 1
    GENDER_TYPE_UNISEX = 2
    GENDER_TYPE_CHOICES = (
        (GENDER_TYPE_FEMALE, 'female'),
        (GENDER_TYPE_MALE, 'male'),
        (GENDER_TYPE_UNISEX, 'unisex'),
    )
    quotation_id =  models.AutoField('id', primary_key=True)
    product_code = models.IntegerField()
    life = models.IntegerField()
    critical_illness = models.IntegerField()
    hospital_expense = models.IntegerField()
    accidental_protection = models.IntegerField()
    accidental_medical_expense = models.IntegerField()
    maturity = models.IntegerField()
    benefit_period = models.IntegerField()
    premium_period = models.IntegerField()
    application_age_min = models.IntegerField()
    application_age_max = models.IntegerField()
    benefit_age_max = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE_CHOICES)
    annual_premium = models.FloatField()
    loading = models.FloatField()

class premium_rate(models.Model):
    GENDER_TYPE_FEMALE = 0
    GENDER_TYPE_MALE = 1
    GENDER_TYPE_UNISEX = 2
    GENDER_TYPE_CHOICES = (
        (GENDER_TYPE_FEMALE, 'female'),
        (GENDER_TYPE_MALE, 'male'),
        (GENDER_TYPE_UNISEX, 'unisex'),
    )
    # SMOKER OR NOT
    FOR_SMOKER = 0
    FOR_NON_SMOKER = 1
    FOR_ALL = 2
    SMOKER_TYPE_CHOICES = (
        (FOR_SMOKER, 'for_smoker'),
        (FOR_NON_SMOKER, 'for_non_smoker'),
        (FOR_ALL, 'it_does_not_matter'),
    )
    id = models.AutoField('id', primary_key=True)
    product_code = models.IntegerField()
    application_age = models.IntegerField(null=True)
    gender = models.IntegerField(choices=GENDER_TYPE_CHOICES)
    smoker = models.IntegerField(choices=SMOKER_TYPE_CHOICES)
    premium_period = models.IntegerField()
    benefit_period = models.IntegerField()
    benefit_age_max = models.IntegerField()
    annual_premium_10k = models.FloatField()

class risk(models.Model):
    GENDER_TYPE_FEMALE = 0
    GENDER_TYPE_MALE = 1
    GENDER_TYPE_UNISEX = 2
    GENDER_TYPE_CHOICES = (
        (GENDER_TYPE_FEMALE, 'female'),
        (GENDER_TYPE_MALE, 'male'),
        (GENDER_TYPE_UNISEX, 'unisex'),
    )
    id = models.AutoField('id', primary_key=True)
    benefit = models.CharField(max_length=32)
    age_min = models.IntegerField()
    age_max = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE_CHOICES)
    probability = models.FloatField()
    institution = models.CharField(max_length=32)
    published = models.DateTimeField(default=django.utils.timezone.now)
    region = models.CharField(max_length=32)
