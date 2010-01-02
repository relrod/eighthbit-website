from bitwik.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

def showpage(request, title):
   # The way this works: User goes to page. If page exists, show it. If not ask if user wants to create it.
   try:
      page = Page.objects.get(slug=title)
   except Page.DoesNotExist:
#      return render_to_response("create.html",{"title": title, "404":True})
      return HttpResponse("does not exist!")

   # And get the latest revision.
   revision = Revision.objects.filter(page=page)[0]

#   return render_to_response("wiki.html",
#         {
#            "title": page.title,
#            "timestamp": revision.timestamp,
#            "local_revision": revision.local_revision,
#            "content": revision.content,
#            "slug": page.slug
#         })
   return HttpResponse("We have: " + page.title+" "+revision.content)

