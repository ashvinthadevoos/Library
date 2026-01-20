from django import forms
from Books.models import Book

class BookAdd(forms.ModelForm):

    class Meta:
        model=Book
        exclude = ["is_active","entry_date"]
        
