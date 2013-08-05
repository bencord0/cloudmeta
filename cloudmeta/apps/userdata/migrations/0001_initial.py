# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Node'
        db.create_table(u'userdata_node', (
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256, primary_key=True)),
            ('userdata', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['userdata.UserData'])),
        ))
        db.send_create_signal(u'userdata', ['Node'])

        # Adding model 'UserData'
        db.create_table(u'userdata_userdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256)),
            ('data', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'userdata', ['UserData'])


    def backwards(self, orm):
        # Deleting model 'Node'
        db.delete_table(u'userdata_node')

        # Deleting model 'UserData'
        db.delete_table(u'userdata_userdata')


    models = {
        u'userdata.node': {
            'Meta': {'object_name': 'Node'},
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256', 'primary_key': 'True'}),
            'userdata': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['userdata.UserData']"})
        },
        u'userdata.userdata': {
            'Meta': {'object_name': 'UserData'},
            'data': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        }
    }

    complete_apps = ['userdata']