from django import forms
from Books.models import Book
from django.contrib.auth.models import User

class BookAdd(forms.ModelForm):

    class Meta:
        model=Book
        exclude = ["is_active","entry_date"]
        
class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username","email","password"]

class SigninForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
