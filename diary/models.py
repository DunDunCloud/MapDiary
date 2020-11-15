from django.db import models, migrations
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    # description = models.CharField(max_length=200,blank=False, default='')
    # published = models.BooleanField(default=False)