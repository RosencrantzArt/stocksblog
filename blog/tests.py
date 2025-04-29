from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Post

class BlogTestCase(TestCase):
    def setUp(self):
      
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='This is a test.', author=self.user)

    def test_create_user(self):
        
        user = User.objects.create_user(username='anotheruser', password='anotherpass')
        self.assertEqual(user.username, 'anotheruser')

    def test_create_post(self):
        
        post = Post.objects.create(title='New Post', content='New content', author=self.user)
        self.assertEqual(post.title, 'New Post')

    def test_post_str_method(self):
        
        self.assertEqual(str(self.post), 'Test Post')

    def test_login_user(self):
        
        login = self.client.login(username='testuser', password='testpass')
        self.assertTrue(login)

    def test_post_list_view_status_code(self):
      
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_status_code(self):
        
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_with_author(self):
       
        self.assertEqual(self.post.author.username, 'testuser')

    def test_post_without_title(self):
        
        with self.assertRaises(ValueError):
            Post.objects.create(title=None, content='Missing title', author=self.user)
