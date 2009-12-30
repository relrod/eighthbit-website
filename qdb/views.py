from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from qdb.models import Quote
from qdb.forms import AddQuote

def showquote(request, id):
   quote = get_object_or_404(Quote, id=id, approved=1)
   return render_to_response('qdb/quote.html', {'quote' : quote})

def addquote(request):
   if request.method == 'POST':
      form = AddQuote(request.POST)
      if form.is_valid():
         newquote = Quote()
         data = form.cleaned_data
         newquote.score = 0
         newquote.submitter = data['submitter']
         newquote.contents = data['contents']
         if data['comment']: 
            newquote.comment = data['comment']
         newquote.approved = 0
         newquote.save()
         #return HttpResponseRedirect('../quote/' + str(newquote.id))
         form = AddQuote()
         return render_to_response('qdb/addquote.html', { 'form' : form, 'saved' : True })
      else:
         return render_to_response('qdb/addquote.html', {'form' : form} )
   else:
      form = AddQuote()
      return render_to_response('qdb/addquote.html', {'form' : form} )
