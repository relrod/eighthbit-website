
from south.db import db
from django.db import models
from qdb.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Quote.votedIPs'
        db.add_column('qdb_quote', 'votedIPs', orm['qdb.quote:votedIPs'])
        
        # Changing field 'Quote.comment'
        # (to signature: django.db.models.fields.CharField(max_length=200, blank=True))
        db.alter_column('qdb_quote', 'comment', orm['qdb.quote:comment'])
        
        # Changing field 'Quote.approved'
        # (to signature: django.db.models.fields.BooleanField(blank=True))
        db.alter_column('qdb_quote', 'approved', orm['qdb.quote:approved'])
        
        # Changing field 'Quote.score'
        # (to signature: django.db.models.fields.IntegerField())
        db.alter_column('qdb_quote', 'score', orm['qdb.quote:score'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Quote.votedIPs'
        db.delete_column('qdb_quote', 'votedIPs')
        
        # Changing field 'Quote.comment'
        # (to signature: models.CharField(max_length=200, null=False, blank=True))
        db.alter_column('qdb_quote', 'comment', orm['qdb.quote:comment'])
        
        # Changing field 'Quote.approved'
        # (to signature: models.BooleanField(editable=False))
        db.alter_column('qdb_quote', 'approved', orm['qdb.quote:approved'])
        
        # Changing field 'Quote.score'
        # (to signature: models.IntegerField(editable=False))
        db.alter_column('qdb_quote', 'score', orm['qdb.quote:score'])
        
    
    
    models = {
        'qdb.quote': {
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'contents': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'submitter': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'votedIPs': ('django.db.models.fields.TextField', [], {})
        }
    }
    
    complete_apps = ['qdb']
