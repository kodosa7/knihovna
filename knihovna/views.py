from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Author
from .models import Book

# Create your views here.

# default home view
def home_view(request):
    return render(request, 'home_view.html', {})

# books list view
def book_list_view(request):
    myqueryset = Book.objects.all()
    context = { 'books': myqueryset }
    return render(request, 'books/book_list.html', context)

# author list view
def author_list_view(request):
    myqueryset = Author.objects.all()
    context = { 'authors': myqueryset }
    return render(request, 'authors/author_list.html', context)

# books by id view
def book_id_view(request, id):
    book = get_object_or_404(Book, id=id)
    context = { 'book': book }
    return render(request, 'books/book_detail.html', context)

# authors by id view
def author_id_view(request, id):
    author = get_object_or_404(Author, id=id)
    context = { 'author': author }
    return render(request, 'authors/author_detail.html', context)

# borrowed books view
def book_borrowed_view(request):
    myqueryset = Book.objects.all()
    context = { 'books': myqueryset }
    return render(request, 'books/book_borrowed.html', context)

# search field view (visible on default home view)
def book_search_view(request):
    searchButtonData = request.GET.get('query')
    searchResult = Book.objects.filter(Q(bookName__icontains=searchButtonData))
    context = { 'books': searchResult }
    return render(request, 'books/book_list.html', context)
