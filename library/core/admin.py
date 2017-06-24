from django.contrib import admin

from .models import Author, Book


class BookInLine(admin.StackedInline):
    model = Book
    extra = 1


class AuthorAdmin(admin.ModelAdmin):
    model = Author
    search_fields = ['name']
    inlines = [BookInLine, ]
    list_display = [field.name for field in Author._meta.fields if field.name != "id"]


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    model = Book
    search_fields = ['name']
    list_display = [field.name for field in Book._meta.fields if field.name != "id"]


admin.site.register(Book, BookAdmin)
