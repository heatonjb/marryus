# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime, timedelta

class Enquiry(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    email = models.EmailField(_('E-mail address'), null=True, blank=True)
    phone = models.CharField(_('Phone Number'), max_length=50, null=True, blank=True)
    subject = models.CharField(_('Phone Number'), max_length=100)
    enquiry = models.TextField(_("Message"))
    date_added = models.DateTimeField(_("date added"), default=datetime.now, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
  
    class Meta:
        verbose_name = _("Contact Form")
        verbose_name_plural = _("Contact Form Enquiries")
        app_label = 'club'