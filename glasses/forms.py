from .models import Eyewear
from django import forms

class EyewearForm(forms.ModelForm):
    class Meta:
        model = Eyewear
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)