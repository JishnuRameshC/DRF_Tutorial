from django.test import TestCase
from .models import Todo
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

class TodoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title="Test Todo", body="Test Body")

    def test_todo_content(self):
        self.assertEqual(self.todo.title, "Test Todo")
        self.assertEqual(self.todo.body, "Test Body")
        self.assertEqual(str(self.todo), "Test Todo")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        
        # Access the first item in the response data to compare with self.todo
        response_data = response.json()[0]
        self.assertEqual(response_data['title'], self.todo.title)
        self.assertEqual(response_data['body'], self.todo.body)

    def test_api_detail_view(self):
        response = self.client.get(reverse("todo_detail", kwargs={'pk': self.todo.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)

        response_data = response.json()
        self.assertEqual(response_data['title'], self.todo.title)
        self.assertEqual(response_data['body'], self.todo.body)
        