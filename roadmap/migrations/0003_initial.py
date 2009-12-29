
from south.db import db
from django.db import models
from roadmap.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Version'
        db.create_table('roadmap_version', (
            ('id', orm['roadmap.Version:id']),
            ('name', orm['roadmap.Version:name']),
        ))
        db.send_create_signal('roadmap', ['Version'])
        
        # Adding model 'Project'
        db.create_table('roadmap_project', (
            ('id', orm['roadmap.Project:id']),
            ('name', orm['roadmap.Project:name']),
            ('description', orm['roadmap.Project:description']),
        ))
        db.send_create_signal('roadmap', ['Project'])
        
        # Adding model 'Stopsign'
        db.create_table('roadmap_stopsign', (
            ('id', orm['roadmap.Stopsign:id']),
            ('what', orm['roadmap.Stopsign:what']),
            ('description', orm['roadmap.Stopsign:description']),
            ('project', orm['roadmap.Stopsign:project']),
            ('percent', orm['roadmap.Stopsign:percent']),
            ('status', orm['roadmap.Stopsign:status']),
        ))
        db.send_create_signal('roadmap', ['Stopsign'])
        
        # Adding ManyToManyField 'Version.project'
        db.create_table('roadmap_version_project', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('version', models.ForeignKey(orm.Version, null=False)),
            ('project', models.ForeignKey(orm.Project, null=False))
        ))
        
        # Adding ManyToManyField 'Stopsign.version'
        db.create_table('roadmap_stopsign_version', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('stopsign', models.ForeignKey(orm.Stopsign, null=False)),
            ('version', models.ForeignKey(orm.Version, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Version'
        db.delete_table('roadmap_version')
        
        # Deleting model 'Project'
        db.delete_table('roadmap_project')
        
        # Deleting model 'Stopsign'
        db.delete_table('roadmap_stopsign')
        
        # Dropping ManyToManyField 'Version.project'
        db.delete_table('roadmap_version_project')
        
        # Dropping ManyToManyField 'Stopsign.version'
        db.delete_table('roadmap_stopsign_version')
        
    
    
    models = {
        'roadmap.project': {
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'roadmap.stopsign': {
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['roadmap.Project']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'version': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['roadmap.Version']"}),
            'what': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'roadmap.version': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'project': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['roadmap.Project']"})
        }
    }
    
    complete_apps = ['roadmap']
