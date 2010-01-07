from bitwik.models import *
from bitwik.forms import EditForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

def showpage(request, title):
   # The way this works: User goes to page. If page exists, show it. If not ask if user wants to create it. << TODO
   try:
      page = Page.objects.get(slug=title)
   except Page.DoesNotExist:
      request.session['404'] = True
      return HttpResponseRedirect("/wiki/" + title + "/edit/")

   # And get the latest revision.
   revision = Revision.objects.filter(page=page).order_by('-id')[0]

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
      revision = Revision.objects.filter(page=page).order_by('-id')[0]
      form = EditForm(instance=revision)
   except Page.DoesNotExist:
      form = EditForm()

   if request.method == 'POST': # Submitted the form.
      form = EditForm(request.POST) # Form contents
      if form.is_valid():
         newrev = form.save(commit=False) # Don't save the form. make a new instance of it.
         newrev.page = page
         newrev.save()
         return HttpResponseRedirect("/wiki/" + title)
      else:
         return render_to_response("bitwik/form.html", {"form": form})
   else:
      return render_to_response("bitwik/form.html", {"form": form})
