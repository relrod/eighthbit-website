from django.contrib import auth
from django.shortcuts import render_to_response, HttpResponse
#from wiki.models import Page
from general.models import Link

def login(request):
   if request.method == "POST":
      username = request.POST.get('username','')
      password = request.POST.get('password','')
      user = auth.authenticate(username=username, password=password)
   
      if user is not None and user.is_active:
         # Password is correct, user is active.
         auth.login(request, user)
         return HttpResponse("You have logged in. In a perfect world, this would redirect to somewhere else")
      else:
         return HttpResponse("did not log in correctly")
   else:
      return render_to_response("registration/login.html")

def front(request):
   links = Link.objects.all()
   frontpage = Page.objects.get(title='front')
   return render_to_response("index.html", {'links':links, 'frontpage':frontpage})

