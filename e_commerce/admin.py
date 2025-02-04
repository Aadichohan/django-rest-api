from django.contrib import admin

# Register your models here.
from e_commerce.models import Author, Categories, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'age',
        'created_at'
    )

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'desc'
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'desc',
        'created_at'
    )

    search_fields = ('title', 'author__name')
    list_filter = ('published_date',)

