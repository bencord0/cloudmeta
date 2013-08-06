# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        for ud in orm.UserData.objects.all():
            # ud is the old UserData model, it does not have the new
            # .save() method to do the stripping for us.
            ud.data = '\n'.join(ud.data.split('\r\n'))
            ud.save()

    def backwards(self, orm):
        # It is save to store stripped userdata
        pass

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
    symmetrical = True
