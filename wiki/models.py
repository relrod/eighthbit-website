from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
   title = models.CharField(max_length=256, unique=True)
   revision = models.ForeignKey('Revision', related_name="page_revision")

   def __unicode__(self):
      return self.title

class Revision(models.Model):
   contents = models.TextField()
   username = models.ForeignKey(User)
   page = models.OneToOneField(Page, related_name="page")
   comment = models.CharField(max_length=256, blank=True)
   
   def __unicode__(self):
      return self.title
