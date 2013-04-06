# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Wedding'
        db.create_table('core_wedding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('ceremony_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('target_amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('external_web_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('sub_title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['Wedding'])

        # Adding model 'Goal'
        db.create_table('core_goal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wedding', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Wedding'])),
            ('amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Goal'])

        # Adding model 'Pledge'
        db.create_table('core_pledge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wedding', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Goal'])),
            ('amount', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('core', ['Pledge'])


    def backwards(self, orm):
        # Deleting model 'Wedding'
        db.delete_table('core_wedding')

        # Deleting model 'Goal'
        db.delete_table('core_goal')

        # Deleting model 'Pledge'
        db.delete_table('core_pledge')


    models = {
        'core.goal': {
            'Meta': {'object_name': 'Goal'},
            'amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'wedding': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Wedding']"})
        },
        'core.pledge': {
            'Meta': {'object_name': 'Pledge'},
            'amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'wedding': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Goal']"})
        },
        'core.wedding': {
            'Meta': {'object_name': 'Wedding'},
            'ceremony_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'external_web_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sub_title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'target_amount': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']