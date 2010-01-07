
from south.db import db
from django.db import models
from bitbin.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Bit'
        db.create_table('bitbin_bit', (
            ('originator', models.ForeignKey(orm['auth.User'])),
            ('text', models.TextField()),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('bitbin', ['Bit'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Bit'
        db.delete_table('bitbin_bit')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'bitbin.bit': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'originator': ('models.ForeignKey', ['User'], {}),
            'text': ('models.TextField', [], {})
        }
    }
    
    complete_apps = ['bitbin']
