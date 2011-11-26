# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Faculty'
        db.create_table('org_faculty', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('university', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['org.University'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal('org', ['Faculty'])

        # Adding unique constraint on 'Faculty', fields ['university', 'name']
        db.create_unique('org_faculty', ['university_id', 'name'])

        # Adding unique constraint on 'Faculty', fields ['university', 'abbr']
        db.create_unique('org_faculty', ['university_id', 'abbr'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Faculty', fields ['university', 'abbr']
        db.delete_unique('org_faculty', ['university_id', 'abbr'])

        # Removing unique constraint on 'Faculty', fields ['university', 'name']
        db.delete_unique('org_faculty', ['university_id', 'name'])

        # Deleting model 'Faculty'
        db.delete_table('org_faculty')


    models = {
        'org.faculty': {
            'Meta': {'unique_together': "(('university', 'name'), ('university', 'abbr'))", 'object_name': 'Faculty'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['org.University']"})
        },
        'org.university': {
            'Meta': {'object_name': 'University'},
            'abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['org']
