
from south.db import db
from django.db import models
from general.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Link'
        db.create_table('general_link', (
            ('id', orm['general.Link:id']),
            ('text', orm['general.Link:text']),
            ('href', orm['general.Link:href']),
        ))
        db.send_create_signal('general', ['Link'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Link'
        db.delete_table('general_link')
        
    
    
    models = {
        'general.link': {
            'href': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['general']
