from django.db import models
from django.contrib.auth.models import User
from random import randint
from hashlib import sha1
from time import time # Time is on my side.
from string import upper

class Bit(models.Model):
   originator = models.ForeignKey(User)
   text = models.TextField()
   private = models.BooleanField()
   key = models.CharField(blank=True, max_length=12)

   def __unicode__(self):
      return "Bit #%s by %s" % (self.id, self.originator)

   def genhash(self):
      """
      Generates a hash to be used as a "key"
      """

      timestamp = str(time)
      random = randint(1,29)
      hex = "0x" + upper(sha1(self.text + timestamp).hexdigest())[random:random+10]
      return hex

   def save(self, *args, **kwargs):
      # If private is true, assign a key.
      # if we ever do symetrical encryption on a paste, do it here...
      # or in the form class, either way.
      if self.private == True:
         self.key = self.genhash()
      
      return super(Bit, self).save(*args, **kwargs)
  
