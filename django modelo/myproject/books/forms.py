from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'rating']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-title', 'placeholder': 'Enter title'}),
            'author': forms.TextInput(attrs={'class': 'input-author', 'placeholder': 'Enter author'}),
            'rating': forms.Select(choices=[(i, str(i)) for i in range(6)], attrs={'class': 'input-rating'}),
        }