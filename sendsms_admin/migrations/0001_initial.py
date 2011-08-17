# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SmsMessage'
        db.create_table('sendsms_admin_smsmessage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_phone', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('to_phones', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('flash', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sent_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal('sendsms_admin', ['SmsMessage'])


    def backwards(self, orm):
        
        # Deleting model 'SmsMessage'
        db.delete_table('sendsms_admin_smsmessage')


    models = {
        'sendsms_admin.smsmessage': {
            'Meta': {'object_name': 'SmsMessage'},
            'body': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'flash': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'from_phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sent_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'to_phones': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        }
    }

    complete_apps = ['sendsms_admin']
