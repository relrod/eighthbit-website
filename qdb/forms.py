from django import forms

class AddQuote(forms.Form):
   submitter = forms.CharField(max_length=50,required=True)
   contents = forms.CharField( widget=forms.widgets.Textarea(), required=True )
   comment = forms.CharField(max_length=200, required=False)
