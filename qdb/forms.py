from django import forms

class AddQuote(forms.Form):
   Submitter = forms.CharField(max_length=50,required=True)
   Contents = forms.CharField( widget=forms.widgets.Textarea(), required=True )
   Comment = forms.CharField(max_length=200, required=False)
