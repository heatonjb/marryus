from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Wedding(models.Model):
    name = models.CharField(_("Name"), max_length=250)
    url = models.URLField(null=True, blank=True)
    ceremony_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    target_amount = models.FloatField(null=True, blank=True)
    external_web_url = models.URLField(null=True, blank=True)
    sub_title = models.CharField(_("Name"), max_length=250)
    description = models.TextField()
    created = models.DateTimeField(_("date added"), default=datetime.now, editable=False)
    updated = models.DateTimeField(auto_now=True)
#    created_by  

class Goal(models.Model):
    wedding = models.ForeignKey(Wedding)
    amount = models.FloatField(null=True, blank=True)
    description = models.TextField()

class Pledge(models.Model):
    wedding = models.ForeignKey(Wedding)
    wedding = models.ForeignKey(Goal)
    amount = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(_("date added"), default=datetime.now, editable=False)
    updated = models.DateTimeField(auto_now=True)
