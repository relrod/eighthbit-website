from django.shortcuts import render_to_response
from wiki.models import Page
from general.models import Link

def front(request):
   links = Link.objects.all()
   frontpage = Page.objects.get(title='front')
   return render_to_response("index.html", {'links':links, 'frontpage':frontpage})

