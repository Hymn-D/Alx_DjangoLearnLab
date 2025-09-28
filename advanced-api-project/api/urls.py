from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
     # List all books OR create a new book
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
     # Retrieve, update, or delete a single book by ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
