
from south.db import db
from django.db import models
from wiki.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Revision'
        db.create_table('wiki_revision', (
            ('username', models.ForeignKey(orm['auth.User'])),
            ('comment', models.CharField(max_length=256, blank=True)),
            ('id', models.AutoField(primary_key=True)),
            ('contents', models.TextField()),
            ('page', models.OneToOneField(orm.Page, related_name=orm.Page)),
        ))
        db.send_create_signal('wiki', ['Revision'])
        
        # Adding model 'Page'
        db.create_table('wiki_page', (
            ('revision', models.ForeignKey(orm.Revision, related_name="page_revision")),
            ('id', models.AutoField(primary_key=True)),
            ('title', models.CharField(unique=True, max_length=256)),
        ))
        db.send_create_signal('wiki', ['Page'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Revision'
        db.delete_table('wiki_revision')
        
        # Deleting model 'Page'
        db.delete_table('wiki_page')
        
    
    
    models = {
        'wiki.revision': {
            'comment': ('models.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'contents': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'page': ('models.OneToOneField', ['Page'], {'related_name': '"page"'}),
            'username': ('models.ForeignKey', ['User'], {})
        },
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'wiki.page': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'revision': ('models.ForeignKey', ["'Revision'"], {'related_name': '"page_revision"'}),
            'title': ('models.CharField', [], {'unique': 'True', 'max_length': '256'})
        }
    }
    
    complete_apps = ['wiki']
