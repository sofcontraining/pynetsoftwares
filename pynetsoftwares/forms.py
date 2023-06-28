from django import forms
from .models import Contactform

class UserContactForm(forms.ModelForm):
    class Meta:
        model = Contactform
        fields = ['name', 'mobile', 'email', 'course', 'msg']