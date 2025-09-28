from django.urls import path
from .views import BookListCreateView, BookDetailView
from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/list', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
]

urlpatterns = [
     # List all books OR create a new book
    path('books/create', BookListCreateView.as_view(), name='book-create'),
]
