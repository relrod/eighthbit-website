
from south.db import db
from django.db import models
from bitwik.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Revision'
        db.create_table('bitwik_revision', (
            ('comment', models.CharField("Revision Comment", max_length=255)),
            ('timestamp', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ('page', models.ForeignKey(orm.Page)),
            ('content', models.TextField()),
            ('editor', models.ForeignKey(orm['auth.User'])),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('bitwik', ['Revision'])
        
        # Adding model 'Page'
        db.create_table('bitwik_page', (
            ('slug', models.SlugField()),
            ('local_revision', models.IntegerField(default=1, editable=False)),
            ('id', models.AutoField(primary_key=True)),
            ('title', models.CharField("Page Title", max_length=255)),
        ))
        db.send_create_signal('bitwik', ['Page'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Revision'
        db.delete_table('bitwik_revision')
        
        # Deleting model 'Page'
        db.delete_table('bitwik_page')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'bitwik.revision': {
            'comment': ('models.CharField', ['"Revision Comment"'], {'max_length': '255'}),
            'content': ('models.TextField', [], {}),
            'editor': ('models.ForeignKey', ['User'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'page': ('models.ForeignKey', ['Page'], {}),
            'timestamp': ('models.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True'})
        },
        'bitwik.page': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'local_revision': ('models.IntegerField', [], {'default': '1', 'editable': 'False'}),
            'slug': ('models.SlugField', [], {}),
            'title': ('models.CharField', ['"Page Title"'], {'max_length': '255'})
        }
    }
    
    complete_apps = ['bitwik']
