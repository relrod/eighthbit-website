from django.template import Library
from qdb.models import Quote

register = Library()

@register.simple_tag
def canvote(ip,id): # format is {% canvote IP ID %}
   quote = get_object_or_404(Quote, id=id)

   if ip in quote.votedIPs.split(','):
      return True
   else:
      return False

