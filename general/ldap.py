from django.contrib.auth.models import User

def ldap_login(userdict): # Expects a dictionary.
   # Go by userdict["username"] and userdict["password"]
   if login_correct:
      # Password is correct, user is active.

      ### THE LOGIN IS CORRECT
      login = True
   else:
      ### THE LOGIN IS NOT CORRECT
      login = False

   return { # FIXME!
         "login": logged_in,
         "is_staff": True
   }

def make_ldap_user(userdict):
   # Create the user object. We'll need to make sure it doesn't
   # exist before trying to create it, but we can do that later.
   # Do some checking from ldap_login, then:
   user = User.objects.create_user(
         userdict["username"],
         userdict["email"],
         userdict["password"]
   )

   if userdict["is_staff"] == True:
      user.is_staff = True

   user.save()
   return user # Let's use this to return the user object.
