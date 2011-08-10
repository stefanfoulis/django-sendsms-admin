#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.contrib import admin
from sendsms import message
from sendsms_admin.models import SmsMessage
from sendsms_admin.backend import DatabaseSmsBackend
from sendsms import api
from django.utils.translation import ugettext as _


class SmsMessageLogAdmin(admin.ModelAdmin):
    date_hierarchy = 'sent_at'
    readonly_fields = ('sent_at', 'to_phones', 'from_phone', 'body', 'flash',)
    list_display = readonly_fields
    def get_model_perms(self, request):
        return {
            'add': False,
            'change': self.has_change_permission(request),
            'delete': False
        }
admin.site.register(SmsMessage, SmsMessageLogAdmin)


class SendSmsMessage(SmsMessage):
    class Meta:
        proxy = True


class SendSmsMessageAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """
        sends the message and does not save it.
        """
        sms_message = message.SmsMessage(
            body=obj.body, from_phone=obj.from_phone,
            to=[t.strip() for t in obj.to_phones.split(',')],
            flash=obj.flash)
        sms_message.send()
        connection = api.get_connection()
        if not isinstance(connection, DatabaseSmsBackend):
            DatabaseSmsBackend().send_messages([sms_message])



    def response_add(self, request, obj, post_url_continue=None):
        """
        returns to the app index instead of to the detail page... because the messages was not saved to the
        database anyway
        """
        msg = _('The SMS was sent successfully.')
        self.message_user(request, msg)
        return HttpResponseRedirect('../../')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def get_model_perms(self, request):
        return {
            'add': self.has_add_permission(request),
            'change': False,
            'delete': False
        }
admin.site.register(SendSmsMessage, SendSmsMessageAdmin)