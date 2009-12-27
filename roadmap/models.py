from django.db import models

PERCENTS = (
   ("0","0%"),
   ("10","10%"), ("20","20%"), ("30","30%"),
   ("40","40%"), ("50","50%"), ("60","60%"),
   ("70","70%"), ("80","80%"), ("90","90%"),
   ("Complete","100%"),
)

STATUSES = (
      ("In Progress/Assigned", "In Progress/Assigned"),
      ("Needs Done - Not Started", "Needs Done- Not Started"),
      ("Excluded/Not Happening", "Excluded/Not Happening"),
      ("Committed/Completed", "Committed/Completed"),
      ("On Hold - Waiting for Feedback", "On Hold - Waiting for Feedback"),
)

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
   project = models.ForeignKey(Project)
   version = models.ManyToManyField(Version)
   percent = models.CharField("Percent Complete", choices=PERCENTS, max_length=3)
   status = models.CharField("Current Status", choices=STATUSES, max_length=20)

   def __unicode__(self):
      return "[%s -> %s] %s" % (self.project.name, self.status, self.what)
   
   class Meta:
      ordering = ('-status',)
