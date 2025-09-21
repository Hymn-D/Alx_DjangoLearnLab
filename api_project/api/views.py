from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, permissions

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()         
    serializer_class = BookSerializer     

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()           
    serializer_class = BookSerializer 
    permission_classes = [permissions.IsAuthenticated]    
    """
        API endpoint for managing books.
        - Requires Token Authentication
        - Permissions:
            * Only authenticated users can access
            * Modify according to custom rules in permissions.py if needed
        """