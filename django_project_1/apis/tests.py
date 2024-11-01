from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book 

# Create your tests here.


class BookAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(title="Test Book", author="Test Author", price=10)

    def test_api_listview(self):
        response = self.client.get('/api/books/')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book')
        self.assertEqual(response.data[0]['author'], 'Test Author')
        self.assertEqual(response.data[0]['price'], 10)
        