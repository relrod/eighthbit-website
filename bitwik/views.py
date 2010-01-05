from bitwik.models import *
from bitwik.forms import EditForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

def showpage(request, title):
   # The way this works: User goes to page. If page exists, show it. If not ask if user wants to create it.
   try:
      page = Page.objects.get(slug=title)
   except Page.DoesNotExist:
      request.session['404'] = True
      return HttpResponseRedirect("/wiki/edit/" + title)

   # And get the latest revision.
   revision = Revision.objects.filter(page=page)[0]

   return render_to_response("bitwik/page.html",
         {
            "title": page.title,
            "timestamp": revision.timestamp,
            "local_revision": revision.local_revision,
            "content": revision.content,
            "comment": revision.comment,
            "slug": page.slug
         })

def edit(request, title):
   try:
      page = Page.objects.get(slug=title)
      revision = Revision.objects.filter(page=page)[0]
      form = EditForm(instance=revision)
   except Page.DoesNotExist:
      form = EditForm()

   return render_to_response("bitwik/form.html", {"form": form, "slug": title} )
