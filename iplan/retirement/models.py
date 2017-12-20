from django.db import models

class city_salary(models.Model):
    id = models.AutoField('id', primary_key=True)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    update_date = models.DateTimeField()
    employee_avg_salary = models.FloatField(null=True)
    retiree_avg_salary = models.FloatField(null=True)
