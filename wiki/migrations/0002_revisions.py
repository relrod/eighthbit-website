
from south.db import db
from django.db import models
from wiki.models import *

class Migration:
    
    def forwards(self, orm):
        "Write your forwards migration here"
    
    
    def backwards(self, orm):
        "Write your backwards migration here"
    
    
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
