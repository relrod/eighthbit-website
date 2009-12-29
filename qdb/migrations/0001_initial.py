
from south.db import db
from django.db import models
from qdb.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Quote'
        db.create_table('qdb_quote', (
            ('id', orm['qdb.Quote:id']),
            ('score', orm['qdb.Quote:score']),
            ('submitter', orm['qdb.Quote:submitter']),
            ('contents', orm['qdb.Quote:contents']),
            ('comment', orm['qdb.Quote:comment']),
        ))
        db.send_create_signal('qdb', ['Quote'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Quote'
        db.delete_table('qdb_quote')
        
    
    
    models = {
        'qdb.quote': {
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'contents': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'submitter': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['qdb']
