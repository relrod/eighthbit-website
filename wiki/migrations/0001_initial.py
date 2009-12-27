
from south.db import db
from django.db import models
from wiki.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Page'
        db.create_table('wiki_page', (
            ('url', models.CharField("URL", max_length=75)),
            ('id', models.AutoField(primary_key=True)),
            ('contents', models.TextField()),
            ('title', models.CharField("Title", max_length=200)),
        ))
        db.send_create_signal('wiki', ['Page'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Page'
        db.delete_table('wiki_page')
        
    
    
    models = {
        'wiki.page': {
            'contents': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'title': ('models.CharField', ['"Title"'], {'max_length': '200'}),
            'url': ('models.CharField', ['"URL"'], {'max_length': '75'})
        }
    }
    
    complete_apps = ['wiki']
