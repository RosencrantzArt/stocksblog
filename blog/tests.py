from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

class SimpleTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')

    def test_create_post(self):
        post = Post.objects.create(title='Test Post', content='Test content')
        self.assertEqual(post.title, 'Test Post')
