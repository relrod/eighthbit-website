
from south.db import db
from django.db import models
from qdb.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Quote.votedIPs'
        db.add_column('qdb_quote', 'votedIPs', models.TextField(default='', null=False, editable=False, blank=True))
        
        # Changing field 'Quote.approved'
        db.alter_column('qdb_quote', 'approved', models.BooleanField())
        
        # Changing field 'Quote.score'
        db.alter_column('qdb_quote', 'score', models.IntegerField())
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Quote.votedIPs'
        db.delete_column('qdb_quote', 'votedIPs')
        
        # Changing field 'Quote.approved'
        db.alter_column('qdb_quote', 'approved', models.BooleanField(default=0, editable=False))
        
        # Changing field 'Quote.score'
        db.alter_column('qdb_quote', 'score', models.IntegerField(default=0, editable=False))
        
    
    
    models = {
        'qdb.quote': {
            'approved': ('models.BooleanField', [], {}),
            'comment': ('models.CharField', [], {'max_length': '200', 'null': 'False', 'blank': 'True'}),
            'contents': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'score': ('models.IntegerField', [], {}),
            'submitter': ('models.CharField', [], {'max_length': '50'}),
            'votedIPs': ('models.TextField', [], {'default': "''", 'null': 'False', 'editable': 'False', 'blank': 'True'})
        }
    }
    
    complete_apps = ['qdb']
