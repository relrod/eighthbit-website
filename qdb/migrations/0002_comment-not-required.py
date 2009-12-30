
from south.db import db
from django.db import models
from qdb.models import *

class Migration:
    
    def forwards(self, orm):
        "Write your forwards migration here"
    
    
    def backwards(self, orm):
        "Write your backwards migration here"
    
    
    models = {
        'qdb.quote': {
            'approved': ('models.BooleanField', [], {}),
            'comment': ('models.CharField', [], {'max_length': '200', 'null': 'False', 'blank': 'True'}),
            'contents': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'score': ('models.IntegerField', [], {}),
            'submitter': ('models.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['qdb']
