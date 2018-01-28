from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Book

class PostForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'author_cognome', 'author_nome',
                'notes', 'publisher', 'pub_year', 'language', 'translation',
                'acquisition_year', 'in_library','borrowed','borrower', 'catalog_date')
        labels = {
            'author_cognome': _('Last Name of Author/Editor:'),
            'author_nome': _('First name of Author/Editor:'),
            'title': _('Title:'),
            'acquisition_year': _('Year acquired:'),
            'in_library': _('In library?'),
            'catalog_date': _('Date cataloged:')
        }
        help_texts = {
            'title': _('Some useful help text.'),
        }
