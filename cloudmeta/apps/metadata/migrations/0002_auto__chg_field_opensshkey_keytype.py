# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'OpensshKey.keytype'
        db.alter_column(u'metadata_opensshkey', 'keytype', self.gf('django.db.models.fields.CharField')(max_length=6))

    def backwards(self, orm):

        # Changing field 'OpensshKey.keytype'
        db.alter_column(u'metadata_opensshkey', 'keytype', self.gf('django.db.models.fields.CharField')(max_length=3))

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