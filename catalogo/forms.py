from django import forms

from .models import Book

class PostForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'notes', 'publisher', 'pub_year')
