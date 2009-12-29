from django.shortcuts import render_to_response, get_object_or_404
from qdb.models import Quote

def showquote(request, id):
   quote  = get_object_or_404(Quote, id=id)
   return render_to_response('qdb/quote.html', {'quote' : quote})
