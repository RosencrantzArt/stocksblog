from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Post, Comment

class BlogTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.admin = User.objects.create_superuser(
            username="admin", password="admin123", email="admin@example.com"
        )
        self.client = Client()
        self.client.login(username="testuser", password="12345")

        self.post = Post.objects.create(
            title="Test Post",
            content="This is test content",
            author=self.user,
            status=1
        )

    def test_user_can_comment_on_post(self):
        comment_count_before = Comment.objects.count()
        response = self.client.post(
            reverse('post_detail', args=[self.post.slug]),
            {'text': 'This is a test comment'}
        )
        comment_count_after = Comment.objects.count()
        self.assertEqual(comment_count_after, comment_count_before + 1)
        comment = Comment.objects.last()
        self.assertFalse(comment.approved)

    def test_anonymous_user_cannot_comment(self):
        self.client.logout()
        comment_count_before = Comment.objects.count()
        response = self.client.post(
            reverse('post_detail', args=[self.post.slug]),
            {'text': 'Anon comment'}
        )
        comment_count_after = Comment.objects.count()
        self.assertEqual(comment_count_after, comment_count_before)

    def test_admin_can_approve_comment(self):
        comment = Comment.objects.create(post=self.post, author=self.user, text="Needs approval")
        self.client.login(username="admin", password="admin123")
        self.client.post(reverse('approve_comment', args=[comment.pk]))
        comment.refresh_from_db()
        self.assertTrue(comment.approved)

    def test_non_admin_cannot_approve_comment(self):
        comment = Comment.objects.create(post=self.post, author=self.user, text="Needs approval")
        response = self.client.post(reverse('approve_comment', args=[comment.pk]))
        comment.refresh_from_db()
        self.assertFalse(comment.approved)
        self.assertNotEqual(response.status_code, 200)

    def test_user_can_delete_own_comment(self):
        comment = Comment.objects.create(post=self.post, author=self.user, text="My comment")
        response = self.client.post(reverse('comment_delete', args=[self.post.slug, comment.pk]))
        self.assertFalse(Comment.objects.filter(pk=comment.pk).exists())

    def test_user_cannot_delete_others_comment(self):
        other_user = User.objects.create_user(username="otheruser", password="test123")
        comment = Comment.objects.create(post=self.post, author=other_user, text="Other comment")
        response = self.client.post(reverse('comment_delete', args=[self.post.slug, comment.pk]))
        self.assertTrue(Comment.objects.filter(pk=comment.pk).exists())
