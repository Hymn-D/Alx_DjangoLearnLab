# relationship_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book, Author, library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect('list_books')
    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})

# Edit a book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_id = request.POST.get('author')
        book.author = get_object_or_404(Author, id=author_id)
        book.save()
        return redirect('list_books')
    authors = Author.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})

# Delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})


