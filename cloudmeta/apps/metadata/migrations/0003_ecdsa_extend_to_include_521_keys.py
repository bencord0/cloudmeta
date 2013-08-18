# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        # Previously, we assumed all ECC keys are 256 bit
        for opensshkey in orm.OpensshKey.objects.filter(keytype="ECC"):
            opensshkey.keytype = "ECC256"
            opensshkey.save()

    def backwards(self, orm):
        # This is an irreversible change,
        # There is no way to (easily) differentiate between 256, 384 and 521 bit ECC keys.
        # There is also no way to store that
        raise RuntimeError("Reversing this migration will cause data loss")

    models = {
        u'metadata.node': {
            'Meta': {'object_name': 'Node'},
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256', 'primary_key': 'True'}),
            'public_keys': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['metadata.OpensshKey']", 'symmetrical': 'False'})
        },
        u'metadata.opensshkey': {
            'Meta': {'object_name': 'OpensshKey'},
            'host': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.TextField', [], {}),
            'keytype': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        }
    }

    complete_apps = ['metadata']
    symmetrical = True
