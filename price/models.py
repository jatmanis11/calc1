from django.db import models
from tinymce.models import HTMLField
from django.db.models import CharField, Model, FileField
from autoslug import AutoSlugField
import datetime

"""class time():
    pass"""
class com_var_data(models.Model):
    sh_price= models.FloatField()
    sh_volume= models.FloatField()

    
class com_static_data(models.Model):
    com_name= models.CharField(max_length=150)
    com_type= models.CharField(max_length= 250)
    com_revenue= models.FloatField()
    com_net_income = models.FloatField()

    news_slug =AutoSlugField(populate_from="com_name",unique=True, null=True, default=None)
# Create your models here.
