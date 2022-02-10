from django.contrib import admin

# Register your models here.
from books_app.books.models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
