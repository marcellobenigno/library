from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AuthorModelForm, BookFormSet
from .models import Author


def home(request):
    return render(request, 'home.html')


def author_list(request):
    authors_list = Author.objects.all()
    selection = request.GET.get('search_box') or None

    if selection is not None:
        authors_list = Author.objects.filter(name__icontains=selection)

    context = {
        'authors_list': authors_list,
    }
    return render(request, 'author/author_listing.html', context)


def author_create(request):
    title = "Criar Novo Autor"
    author_form = AuthorModelForm(request.POST or None)
    author = Author()
    formset = BookFormSet(request.POST or None, instance=author, prefix='book')

    if author_form.is_valid():
        created_author = author_form.save(commit=False)
        formset = BookFormSet(request.POST, instance=created_author, prefix='book')
        if formset.is_valid():
            created_author.save()
            formset.save()
        messages.success(request,
                         'Autor cadastrado com sucesso!')
        return redirect('core:author_list')

    context = {
        'title': title,
        'form': author_form,
        'formset': formset,
    }
    return render(request, 'author/author_form.html', context)


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author/author_detail.html', {'author': author})


def author_edit(request, pk):
    title = "Editar Autor"
    author = get_object_or_404(Author, pk=pk)
    author_form = AuthorModelForm(request.POST or None, instance=author)
    formset = BookFormSet(request.POST or None, instance=author, prefix='book')

    if author_form.is_valid():
        created_author = author_form.save(commit=False)
        formset = BookFormSet(request.POST, instance=created_author, prefix='book')
        if formset.is_valid():
            created_author.save()
            formset.save()
        messages.success(request,
                         'Autor cadastrado com sucesso!')
        return redirect('core:author_list')

    context = {
        'title': title,
        'form': author_form,
        'formset': formset,
    }
    return render(request, 'author/author_form.html', context)


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == 'POST':
        author.delete()
        messages.success(request,
                         'Autor apagado com sucesso!')
        return redirect('core:author_list')

    return render(request, 'author/autor_delete.html', {'author': author})
