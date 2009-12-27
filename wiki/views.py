from eighthbit.wiki.models import Page
from django.shortcuts import get_object_or_404, render_to_response

def showpage(request, page):
    wikipage = get_object_or_404(Page, title__iexact=page)
    return render_to_response("wiki.html", {'wiki': wikipage})

