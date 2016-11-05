# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FlowFile.final_file'
        db.add_column('flowjs_flowfile', 'final_file',
                      self.gf('django.db.models.fields.files.FileField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FlowFile.final_file'
        db.delete_column('flowjs_flowfile', 'final_file')


    models = {
        'flowjs.flowfile': {
            'Meta': {'object_name': 'FlowFile'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'final_file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'total_chunks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_chunks_uploaded': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'flowjs.flowfilechunk': {
            'Meta': {'ordering': "['number']", 'object_name': 'FlowFileChunk'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'chunks'", 'to': "orm['flowjs.FlowFile']"})
        }
    }

    complete_apps = ['flowjs']