from django.db import models
from django.contrib.auth.models import User

class Bit(models.Model):
   originator = models.ForeignKey(User)
   text = models.TextField()

   def __unicode__(self):
      return "Bit #%s by %s" % (self.id, self.originator)

