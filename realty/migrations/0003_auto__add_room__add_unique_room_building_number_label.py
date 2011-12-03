# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Room'
        db.create_table('realty_room', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('building', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['realty.Building'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('floor', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('realty', ['Room'])

        # Adding unique constraint on 'Room', fields ['building', 'number', 'label']
        db.create_unique('realty_room', ['building_id', 'number', 'label'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Room', fields ['building', 'number', 'label']
        db.delete_unique('realty_room', ['building_id', 'number', 'label'])

        # Deleting model 'Room'
        db.delete_table('realty_room')


    models = {
        'org.university': {
            'Meta': {'object_name': 'University'},
            'abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'realty.building': {
            'Meta': {'unique_together': "(('university', 'number', 'label'),)", 'object_name': 'Building'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'university': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['org.University']"})
        },
        'realty.room': {
            'Meta': {'unique_together': "(('building', 'number', 'label'),)", 'object_name': 'Room'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['realty.Building']"}),
            'floor': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['realty']
