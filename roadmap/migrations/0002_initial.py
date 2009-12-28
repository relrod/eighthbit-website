
from south.db import db
from django.db import models
from roadmap.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Version'
        db.create_table('roadmap_version', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField("Version", max_length=15)),
        ))
        db.send_create_signal('roadmap', ['Version'])
        
        # Adding model 'Project'
        db.create_table('roadmap_project', (
            ('description', models.TextField("Description")),
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField("Project Name", max_length=100)),
        ))
        db.send_create_signal('roadmap', ['Project'])
        
        # Adding model 'Stopsign'
        db.create_table('roadmap_stopsign', (
            ('status', models.CharField("Current Status", max_length=20)),
            ('what', models.CharField("What is going to happen", max_length=255)),
            ('description', models.TextField("Extra Details")),
            ('percent', models.CharField("Percent Complete", max_length=3)),
            ('project', models.ForeignKey(orm.Project)),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('roadmap', ['Stopsign'])
        
        # Adding ManyToManyField 'Version.project'
        db.create_table('roadmap_version_project', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('version', models.ForeignKey(Version, null=False)),
            ('project', models.ForeignKey(Project, null=False))
        ))
        
        # Adding ManyToManyField 'Stopsign.version'
        db.create_table('roadmap_stopsign_version', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('stopsign', models.ForeignKey(Stopsign, null=False)),
            ('version', models.ForeignKey(Version, null=False))
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
        'roadmap.version': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', ['"Version"'], {'max_length': '15'}),
            'project': ('models.ManyToManyField', ['Project'], {})
        },
        'roadmap.project': {
            'description': ('models.TextField', ['"Description"'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', ['"Project Name"'], {'max_length': '100'})
        },
        'roadmap.stopsign': {
            'Meta': {'ordering': "('-status',)"},
            'description': ('models.TextField', ['"Extra Details"'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'percent': ('models.CharField', ['"Percent Complete"'], {'max_length': '3'}),
            'project': ('models.ForeignKey', ['Project'], {}),
            'status': ('models.CharField', ['"Current Status"'], {'max_length': '20'}),
            'version': ('models.ManyToManyField', ['Version'], {}),
            'what': ('models.CharField', ['"What is going to happen"'], {'max_length': '255'})
        }
    }
    
    complete_apps = ['roadmap']
