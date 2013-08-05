# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Node'
        db.create_table(u'metadata_node', (
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256, primary_key=True)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal(u'metadata', ['Node'])

        # Adding M2M table for field public_keys on 'Node'
        m2m_table_name = db.shorten_name(u'metadata_node_public_keys')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('node', models.ForeignKey(orm[u'metadata.node'], null=False)),
            ('opensshkey', models.ForeignKey(orm[u'metadata.opensshkey'], null=False))
        ))
        db.create_unique(m2m_table_name, ['node_id', 'opensshkey_id'])

        # Adding model 'OpensshKey'
        db.create_table(u'metadata_opensshkey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256)),
            ('keytype', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('key', self.gf('django.db.models.fields.TextField')()),
            ('host', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal(u'metadata', ['OpensshKey'])


    def backwards(self, orm):
        # Deleting model 'Node'
        db.delete_table(u'metadata_node')

        # Removing M2M table for field public_keys on 'Node'
        db.delete_table(db.shorten_name(u'metadata_node_public_keys'))

        # Deleting model 'OpensshKey'
        db.delete_table(u'metadata_opensshkey')


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
            'keytype': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        }
    }

    complete_apps = ['metadata']