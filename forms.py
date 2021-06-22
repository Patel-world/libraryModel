from django import forms
from .models import BookSearch


class BookSearchForm(forms.ModelForm):
    name_of_book = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Enter name of book'
    }))
    class Meta:
        model = BookSearch
        fields = ['name_of_book',]

class NotesSearchForm(forms.ModelForm):
    name_of_subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control me-2", 'placeholder': 'Enter name of subject'
    }))
    class Meta:
        model = NoteSearch
        fields = ['name_of_subject',]