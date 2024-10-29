from django.test import TestCase
from .models import Book
# Create your tests here.

class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(title="Test Book", author="Test Author", price=10)

    def test_book_content(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.price, 10)
    
    def test_book_list_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')
        self.assertTemplateUsed(response, 'books/book_list.html')

