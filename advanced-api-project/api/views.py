from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


# GET all books, POST new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# GET one book, PUT/PATCH update, DELETE book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

