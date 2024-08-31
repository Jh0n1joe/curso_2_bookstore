from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('q', '')  # Obtener el término de búsqueda
        if query:
            return Book.objects.filter(title__icontains=query)  # Filtrar libros por título
        return Book.objects.all()  # Si no hay búsqueda, mostrar todos los libros

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
