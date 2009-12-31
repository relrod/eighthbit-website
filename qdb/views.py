from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from qdb.models import Quote
from qdb.forms import AddQuote

def list(request, page):
   quotes = Quote.objects.filter(approved=1)
   paginator = Paginator(quotes, 25)

   try:
      quotepage = paginator.page(page)
   except (EmptyPage, InvalidPage):
      quotepage = paginator.page(paginator.num_pages)

   return render_to_response("qdb/list.html", {"quotes" : quotepage})

def showquote(request, id):
   if id == "random":
      quote = Quote.objects.all().order_by('?')[:1].get()
   else:
      quote = get_object_or_404(Quote, id=id, approved=1)
   return render_to_response('qdb/quote.html', {'quote' : quote})

def addquote(request):
   if request.method == 'POST':
      form = AddQuote(request.POST)
      if form.is_valid():
         initial = form.save(commit=False)
         initial.approved = 0
         initial.score = 0
         initial.save()
         form.save_m2m()
         form = AddQuote()
         return render_to_response('qdb/addquote.html', { 'form' : form, 'saved' : True })
      else:
         return render_to_response('qdb/addquote.html', {'form' : form} )
   else:
      form = AddQuote()
      return render_to_response('qdb/addquote.html', {'form' : form} )


def vote(request, id, direction):
   quote = get_object_or_404(Quote, id=id)
   if direction == "up":
      quote.score += 1
   elif direction == "down":
      quote.score -= 1
  
   quote.save()
   return HttpResponse(str(quote.score))
