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


