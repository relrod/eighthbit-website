from django.db import models

class Quote(models.Model):
   score = models.IntegerField()
   submitter = models.CharField(max_length=50)
   contents = models.TextField()
   comment = models.CharField(max_length=200, blank=True, null=False)
   approved = models.BooleanField()
   votedIPs = models.TextField(default='', blank=True, null=False, editable=False) #This is just a comma seperated list for ow. Subject to change.
   def __unicode__(self):
      return "#%s by %s" % (self.id, self.submitter)
