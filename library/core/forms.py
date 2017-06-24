from django.forms import ModelForm, inlineformset_factory

from .models import Author, Book


class AuthorModelForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name',)


BookFormSet = inlineformset_factory(Author, Book, fields=('title',), extra=3)
