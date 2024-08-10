from django.contrib import admin
from .models import Book, Review

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    list_filter = ('author',)
    search_fields = ('title', 'author',)
    ordering = ('title','price',)
    inlines = [ ReviewInline, ]



admin.site.register(Book, BookAdmin)