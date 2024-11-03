from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
# Create your tests here.

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            password='12345',
            name='testuser',
        )
        cls.post = Post.objects.create(
            title='Test Post',
            body='Test Post Body',
            author=cls.user
        )

    def test_blog_content(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.body, 'Test Post Body')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(str(self.post), 'Test Post')
