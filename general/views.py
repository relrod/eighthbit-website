from django.contrib import auth
from django.shortcuts import render_to_response, HttpResponse
#from wiki.models import Page
from general.models import Link
from general.ldap import *

def login(request):
   if request.method != "POST":
      return render_to_response("registration/login.html")

   attemptlogin = ldap_login(
         request.POST.get("username",""),
         request.POST.get("password","")
   )

   if attemptlogin["login"] == True:
      auth.login(request, make_ldap_user(username))
   else:
      # Failed login.


def front(request):
   links = Link.objects.all()
   frontpage = Page.objects.get(title='front')
   return render_to_response("index.html", {'links':links, 'frontpage':frontpage})

