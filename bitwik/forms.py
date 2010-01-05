from django import forms
from django.forms import ModelForm
from bitwik.models import Page, Revision

class EditForm(ModelForm):
   class Meta:
      model = Revision
      exclude = ("page")
   
   title = forms.CharField(max_length=255)

