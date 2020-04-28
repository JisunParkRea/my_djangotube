from django.test import TestCase
from django.contrib.auth.models import User

from video.models import Video


class VideoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user = User.objects.create_user(username='test_user', email='test_user@example.com', password='test_password')
        Video.objects.create(author=test_user, title='코로나 국민예방수칙', category='info', video_key='G7rBBWeunHM')

    def test_title_label(self):
        video = Video.objects.get(id=1)
        field_label = video._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        video = Video.objects.get(id=1)
        max_length = video._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_default_count_likes_user_is_zero(self):
        video = Video.objects.get(id=1)
        default_count_likes_user = video.count_likes_user()
        self.assertEquals(default_count_likes_user, 0)

    def test_object_name_is_title(self):
        video = Video.objects.get(id=1)
        expected_object_name = video.title
        self.assertEquals(expected_object_name, str(video.title))

