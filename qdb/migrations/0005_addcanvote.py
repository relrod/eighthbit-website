
from south.db import db
from django.db import models
from qdb.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Quote.canvote'
        db.add_column('qdb_quote', 'canvote', orm['qdb.quote:canvote'])
        
        # Changing field 'Quote.votedIPs'
        # (to signature: django.db.models.fields.TextField(blank=True))
        db.alter_column('qdb_quote', 'votedIPs', orm['qdb.quote:votedIPs'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Quote.canvote'
        db.delete_column('qdb_quote', 'canvote')
        
        # Changing field 'Quote.votedIPs'
        # (to signature: django.db.models.fields.TextField())
        db.alter_column('qdb_quote', 'votedIPs', orm['qdb.quote:votedIPs'])
        
    
    
    models = {
        'qdb.quote': {
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'canvote': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'contents': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'submitter': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'votedIPs': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        }
    }
    
    complete_apps = ['qdb']
