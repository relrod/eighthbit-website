from string import replace
from django.db import models
from django.contrib.auth.models import User
from helperfuncs import slugify

class Page(models.Model):
   title = models.CharField("Page Title", max_length=255)
   slug = models.SlugField(editable=False)
   local_revision = models.IntegerField(default=0, editable=False)

   def save(self, *args, **kwargs):
      self.slug = slugify(self.title, instance=self)
      super(Page, self).save(*args, **kwargs)

   def __unicode__(self):
      return "%s" % self.title

class Revision(models.Model):
   page = models.ForeignKey(Page)
   editor = models.ForeignKey(User)
   content = models.TextField()
   comment = models.CharField("Revision Comment", max_length=255)
   timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
   local_revision = models.IntegerField(editable=False, default=0)
   
   def save(self, *args, **kwargs):
      pg = self.page
      pg.local_revision += 1
      pg.save()
      self.local_revision = pg.local_revision

      super(Revision, self).save(*args, **kwargs)

   def __unicode__(self):
      return "r%s of %s" % (self.local_revision, self.page.title)
