from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

class AuthorBookInline(admin.TabularInline):
    model = Book
    extra = 0

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = [('last_name', 'first_name'), ('date_of_birth', 'date_of_death')]

    inlines = [AuthorBookInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# Register the Admin class for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('Book Instance Information', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

#admin.site.register(Book)
#admin.site.register(Author)
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)