#-*- coding: utf-8 -*-
from sendsms.backends.base import BaseSmsBackend
from sendsms_admin.models import SmsMessage


class DatabaseSmsBackend(BaseSmsBackend):
    def send_messages(self, messages):
        for message in messages:
            SmsMessage.objects.create(
                body=message.body,
                from_phone=message.from_phone,
                to_phones=', '.join(message.to),
                flash=message.flash
            )