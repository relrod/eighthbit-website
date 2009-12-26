from django.db import models

class Link(models.Model):
   text = models.CharField("Link Text", max_length=100)
   href = models.CharField("Link HREF", max_length=255)

   def __unicode__(self):
      return self.text

