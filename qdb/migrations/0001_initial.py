
from south.db import db
from django.db import models
from qdb.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Quote'
        db.create_table('qdb_quote', (
            ('comment', models.CharField(max_length=200)),
            ('approved', models.BooleanField()),
            ('score', models.IntegerField()),
            ('submitter', models.CharField(max_length=50)),
            ('id', models.AutoField(primary_key=True)),
            ('contents', models.TextField()),
        ))
        db.send_create_signal('qdb', ['Quote'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Quote'
        db.delete_table('qdb_quote')
        
    
    
    models = {
        'qdb.quote': {
            'approved': ('models.BooleanField', [], {}),
            'comment': ('models.CharField', [], {'max_length': '200'}),
            'contents': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'score': ('models.IntegerField', [], {}),
            'submitter': ('models.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['qdb']
