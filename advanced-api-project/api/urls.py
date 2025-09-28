from django.urls import path
from .views import BookListCreateView, BookDetailView
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]

urlpatterns = [
     # List all books OR create a new book
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
]
