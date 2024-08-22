from django.db import models

class Employee(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=15)
    empaddress=models.CharField(max_length=25)

