from django.forms import ModelForm, inlineformset_factory

from .models import Author, Book


class AuthorModelForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'summary']


BookFormSet = inlineformset_factory(Author, Book, form=BookModelForm, extra=1)
