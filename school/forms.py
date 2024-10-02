from django import forms
from .models import photo

class photoform(forms.ModelForm):
    class Meta:
        model = photo
        fields = ['title','description','image']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)        
    