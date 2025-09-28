def test_create_book_authenticated(self):
    self.client.force_authenticate(user=self.user)
    response = self.client.post('/books/create/', data={...})
    self.assertEqual(response.status_code, 201)

def test_update_book_unauthenticated(self):
    response = self.client.put('/books/1/update/', data={...})
    self.assertEqual(response.status_code, 403)

def test_filter_books_by_author(self):
    response = self.client.get('/books/?author=1')
    self.assertEqual(response.status_code, 200)
    self.assertTrue(all(book['author'] == 1 for book in response.data))

def test_search_books_by_title(self):
    response = self.client.get('/books/?search=Things')
    self.assertEqual(response.status_code, 200)
    self.assertTrue(any('Things' in book['title'] for book in response.data))

def test_order_books_by_year_desc(self):
    response = self.client.get('/books/?ordering=-publication_year')
    self.assertEqual(response.status_code, 200)
    years = [book['publication_year'] for book in response.data]
    self.assertEqual(years, sorted(years, reverse=True))

def test_delete_book_unauthenticated(self):
    response = self.client.delete('/books/1/delete/')
    self.assertEqual(response.status_code, 403)

def test_delete_book_authenticated(self):
    self.client.force_authenticate(user=self.user)
    response = self.client.delete('/books/1/delete/')
    self.assertEqual(response.status_code, 204)
