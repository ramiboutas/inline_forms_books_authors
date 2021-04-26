from django import forms
from django.forms.models import inlineformset_factory
from books.models import Author, Book



AuthorBooksFormSet = inlineformset_factory(Author, Book, fields=('title', ))
