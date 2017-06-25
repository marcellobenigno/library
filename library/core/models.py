from django.db import models


class Author(models.Model):
    name = models.CharField('nome', max_length=100, unique=True)

    class Meta:
        verbose_name = 'autor'
        verbose_name_plural = 'autores'
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, verbose_name='autor', on_delete=models.CASCADE)
    title = models.CharField('título', max_length=100)
    summary = models.TextField('sumário', max_length=600, blank=True)

    class Meta:
        verbose_name = 'livro'
        verbose_name_plural = 'livros'
        ordering = ['title']

    def __str__(self):
        return self.title
