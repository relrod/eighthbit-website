from bitbin.models import *
from django.shortcuts import get_object_or_404, render_to_response

def paste(request, id):
   paste = get_object_or_404(Bit, id=id)
   return render_to_response("bitbin/view.html", {"paste": paste})

