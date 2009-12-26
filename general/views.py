from django.shortcuts import render_to_response
from general.models import Link

def front(request):
   links = Link.objects.all()
   return render_to_response("index.html", {'links':links})

