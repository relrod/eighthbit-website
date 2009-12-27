
from south.db import db
from django.db import models
from general.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Link'
        db.create_table('general_link', (
            ('text', models.CharField("Link Text", max_length=100)),
            ('href', models.CharField("Link HREF", max_length=255)),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('general', ['Link'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Link'
        db.delete_table('general_link')
        
    
    
    models = {
        'general.link': {
            'href': ('models.CharField', ['"Link HREF"'], {'max_length': '255'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'text': ('models.CharField', ['"Link Text"'], {'max_length': '100'})
        }
    }
    
    complete_apps = ['general']
