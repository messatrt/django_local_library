from django.contrib import admin

# Register your models here.
from .models import Author, Language, Book, BookInstance, Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(BookInstance)
admin.site.register(Genre)
