from django.db import models

class Page(models.Model):
   title = models.CharField("Title", max_length=200)
   url = models.CharField("URL", max_length=75)
   contents = models.TextField()
   
   def __unicode__(self):
      return self.title
