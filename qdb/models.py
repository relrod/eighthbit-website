from django.db import models

class Quote(models.Model):
   score = models.IntegerField()
   submitter = models.CharField(max_length=50)
   contents = models.TextField()
   comment = models.CharField(max_length=200, blank=True, null=False)
   approved = models.BooleanField()

   def __unicode__(self):
      return "#%s by %s" % (self.id, self.submitter)

class Vote(models.Model):
   ip = models.IPAddressField("IP")
   quote = models.ForeignKey(Quote) # The quote we're voting on.
   direction = models.BooleanField() # True = +, False = -

   def save(self, *args, **kwargs):
      quote = self.quote
      if self.direction == True:
         quote.score += 1
      else:
         quote.score -= 1

      quote.save()
      super(Vote, self).save(*args, **kwargs)

   def txt_direction(self, symbol=False):
      if self.direction == True:
         return "positive" if not symbol else "+"
      else:
         return "negative" if not symbol else "-"

   def quoteid(self):
      return self.quote.id

   def __unicode__(self):
      return "Quote# %s (%s vote from IP %s)" % (self.quoteid(), self.txt_direction(), self.ip)
