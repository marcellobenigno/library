from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book
from .forms import AuthorModelForm


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
    form = AuthorModelForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request,
                         'Autor cadastrado com sucesso!')
        return redirect('core:author_list')

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'author/author_form.html', context)


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author/author_detail.html', {'author': author})


def author_edit(request, pk):
    title = "Editar Autor"
    author = get_object_or_404(Author, pk=pk)
    form = AuthorModelForm(request.POST or None, instance=author)

    if form.is_valid():
        form.save()
        messages.success(request,
                         'Autor editado com sucesso!')
        return redirect('core:author_list')

    context = {
        'title': title,
        'form': form
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
