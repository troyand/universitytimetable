# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'University'
        db.create_table('org_university', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('abbr', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16)),
        ))
        db.send_create_signal('org', ['University'])


    def backwards(self, orm):
        
        # Deleting model 'University'
        db.delete_table('org_university')


    models = {
        'org.university': {
            'Meta': {'object_name': 'University'},
            'abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['org']
