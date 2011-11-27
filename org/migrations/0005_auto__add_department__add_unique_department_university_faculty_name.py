# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Department'
        db.create_table('org_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('university', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['org.University'], null=True, blank=True)),
            ('faculty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['org.Faculty'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('org', ['Department'])

        # Adding unique constraint on 'Department', fields ['university', 'faculty', 'name']
        db.create_unique('org_department', ['university_id', 'faculty_id', 'name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Department', fields ['university', 'faculty', 'name']
        db.delete_unique('org_department', ['university_id', 'faculty_id', 'name'])

        # Deleting model 'Department'
        db.delete_table('org_department')


    models = {
        'org.department': {
            'Meta': {'unique_together': "(('university', 'faculty', 'name'),)", 'object_name': 'Department'},
            'faculty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['org.Faculty']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['org.University']", 'null': 'True', 'blank': 'True'})
        },
        'org.faculty': {
            'Meta': {'unique_together': "(('university', 'name'), ('university', 'abbr'))", 'object_name': 'Faculty'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['org.University']"})
        },
        'org.major': {
            'Meta': {'unique_together': "(('faculty', 'name', 'kind'),)", 'object_name': 'Major'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'faculty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['org.Faculty']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'org.university': {
            'Meta': {'object_name': 'University'},
            'abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['org']
