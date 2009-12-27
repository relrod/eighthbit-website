from django.db import models

class Project(models.Model):
   name = models.CharField("Project Name", max_length=100)
   description = models.TextField("Description")
   
   def __unicode__(self):
      return self.name

class Version(models.Model):
   name = models.CharField("Version", max_length=15)
   project = models.ManyToManyField(Project)

   def __unicode__(self):
      return self.name

class Stopsign(models.Model):
   what = models.CharField("What is going to happen", max_length=255)
   description = models.TextField("Extra Details")
   project = models.ManyToManyField(Project)
   version = models.ManyToManyField(Version)

   def __unicode__(self):
      return "[%s] %s" % (self.project, self.what)

class Roadbump(models.Model):
   what = models.CharField("What is the problem", max_length=255)
   description = models.TextField("Extra Details")
   project = models.ManyToManyField(Project)
   stopsign = models.ManyToManyField(Stopsign)
   oldversion = models.ForeignKey(Version, related_name="old_version")
   newversion = models.ForeignKey(Version, related_name="new_version")

   def __unicode__(self):
      return "[%s] %s - %s -> %s" % (self.project, self.what, self.oldversion, self.newversion)

