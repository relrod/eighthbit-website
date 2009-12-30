from django.forms import ModelForm
from qdb.models import Quote

class AddQuote(ModelForm):
   class Meta:
      model = Quote
      exclude = ['approved','score']

  # submitter = forms.CharField(max_length=50,required=True)
  # contents = forms.CharField( widget=forms.widgets.Textarea(), required=True )
  # comment = forms.CharField(max_length=200, required=False)
