
from south.db import db
from django.db import models
from bitwik.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Revision.local_revision'
        db.alter_column('bitwik_revision', 'local_revision', models.IntegerField(default=0, editable=False))
        
        # Changing field 'Page.local_revision'
        db.alter_column('bitwik_page', 'local_revision', models.IntegerField(default=0, editable=False))
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Revision.local_revision'
        db.alter_column('bitwik_revision', 'local_revision', models.IntegerField(default=1, editable=False))
        
        # Changing field 'Page.local_revision'
        db.alter_column('bitwik_page', 'local_revision', models.IntegerField(default=1, editable=False))
        
    
    
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
            'local_revision': ('models.IntegerField', [], {'default': '0', 'editable': 'False'}),
            'page': ('models.ForeignKey', ['Page'], {}),
            'timestamp': ('models.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True'})
        },
        'bitwik.page': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'local_revision': ('models.IntegerField', [], {'default': '0', 'editable': 'False'}),
            'slug': ('models.SlugField', [], {'editable': 'False'}),
            'title': ('models.CharField', ['"Page Title"'], {'max_length': '255'})
        }
    }
    
    complete_apps = ['bitwik']
