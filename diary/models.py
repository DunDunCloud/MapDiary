from django.db import models, migrations
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    place_name = models.CharField(max_length=70, blank=False, default='')
    place_addr = models.CharField(max_length=200, blank=False, default='')
    description = models.CharField(max_length=600,blank=False, default='')
    writer = models.CharField(max_length=70,blank=False, default='')
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)
    published_date = models.DateTimeField(auto_now_add=True)
#     사진 url 추가 필요
