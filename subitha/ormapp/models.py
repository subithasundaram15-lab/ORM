from django.db import models
from django.contrib import admin

class cardb(models.Model):
    car_name=models.CharField(max_length=30)
    regno=models.IntegerField(primary_key=True)
    carowner_email=models.EmailField()
    date=models.DateField()
    mileage=models.FloatField()
    colour=models.CharField(max_length=20)
class cardb_admin(admin.ModelAdmin):
    list_display=['car_name','regno','carowner_email','date','mileage','colour']
