from django.template import Library
from qdb.models import Quote

register = Library()

@register.inclusion_tag("qdb/list.html")
def canvote(parser, token): # format is {% canvote IP ID %}
   tagname, ip, id = token.split_contents()
   quote = get_object_or_404(Quote, id=id)

   if ip in quote.votedIPs.split(','):
      return True
   else:
      return False


