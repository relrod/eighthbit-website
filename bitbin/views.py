from bitbin.models import *
from django.shortcuts import get_object_or_404, render_to_response

def paste(request, id):
   if id[0] == "0" and id[1] == "x":
      # Assume private paste.
      paste = get_object_or_404(Bit, key=id)
   else:
      paste = get_object_or_404(Bit, id=id, key="")
   return render_to_response("bitbin/view.html", {"paste": paste})

