# LibraryProject/bookshelf/admin.py

from django.contrib import admin
from .models import Book # Import your Book model

# Register your models here.

# Define the custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') # Columns displayed in the list view
    list_filter = ('publication_year',) # Filters on the sidebar
    search_fields = ('title', 'author') # Fields to search against

# Register the Book model with its custom admin class
admin.site.register(Book, BookAdmin)