#-*- coding: utf-8 -*-
from django.db import models

class SmsMessage(models.Model):
    from_phone = models.CharField(max_length=255, blank=True, default='')
    to_phones = models.TextField(blank=True, default='')
    body = models.TextField(blank=True, default='')
    flash = models.BooleanField(default=False)

    sent_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)