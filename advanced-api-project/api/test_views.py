from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='esther', password='testpass')
        self.author = Author.objects.create(name='Chinua Achebe')
        self.book = Book.objects.create(
            title='Things Fall Apart',
            publication_year=1958,
            author=self.author
        )

    def test_list_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'No Longer at Ease',
            'publication_year': 1960,
            'author': self.author.id
        }
        response = self.client.post('/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book_unauthenticated(self):
        data = {'title': 'Updated Title'}
        response = self.client.put(f'/books/{self.book.id}/update/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books_by_year(self):
        response = self.client.get('/books/?publication_year=1958')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        response = self.client.get('/books/?search=Things')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Things' in book['title'] for book in response.data))

    def test_order_books_by_title(self):
        response = self.client.get('/books/?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
