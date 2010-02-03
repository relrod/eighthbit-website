
from south.db import db
from django.db import models
from qdb.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Vote'
        db.create_table('qdb_vote', (
            ('id', orm['qdb.vote:id']),
            ('ip', orm['qdb.vote:ip']),
            ('quote', orm['qdb.vote:quote']),
            ('direction', orm['qdb.vote:direction']),
        ))
        db.send_create_signal('qdb', ['Vote'])
        
        # Deleting field 'Quote.votedIPs'
        db.delete_column('qdb_quote', 'votedIPs')
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Vote'
        db.delete_table('qdb_vote')
        
        # Adding field 'Quote.votedIPs'
        db.add_column('qdb_quote', 'votedIPs', orm['qdb.quote:votedIPs'])
        
    
    
    models = {
        'qdb.quote': {
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'contents': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'submitter': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'qdb.vote': {
            'direction': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'quote': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['qdb.Quote']"})
        }
    }
    
    complete_apps = ['qdb']
