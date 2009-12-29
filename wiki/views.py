from eighthbit.wiki.models import Page
from django.shortcuts import get_object_or_404, render_to_response

def showpage(request, Title):
    wikipage = get_object_or_404(title, url__iexact=Title)
    return render_to_response("wiki.html", {'wiki': wikipage})

