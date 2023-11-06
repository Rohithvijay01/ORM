
from django.db import models
from django.contrib import admin
class players (models.Model):
    playerid=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    score=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()
class playersAdmin(admin.ModelAdmin):
    list_display=('playerid','name','score','age','email')
# Create your models here.
