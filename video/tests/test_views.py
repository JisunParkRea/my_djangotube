from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from video.models import Video
from video.views import my_video

class VideoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user = User.objects.create_user(username='test_user', email='test_user@example.com', password='test_password')
        Video.objects.create(author=test_user, title='코로나 국민예방수칙', category='info', video_key='G7rBBWeunHM')
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/video/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('video_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('video_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'video/video_list.html')

class MyVideoListViewTest(TestCase):
    def setUp(self):
        # Create user
        test_user = User.objects.create_user(username='test_user', email='test_user@example.com', password='test_password')

        test_user.save()

        # Create video
        Video.objects.create(author=test_user, title='코로나 국민예방수칙', category='info', video_key='G7rBBWeunHM')
        
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('my_video'))
        self.assertRedirects(response, '/video/login/?next=/video/myVideo/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('my_video'))
        
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'test_user')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'video/my_video.html')
