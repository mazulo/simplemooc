from django.test import TestCase
from simplemooc.courses.models import Course
from model_mommy import mommy


class ContactCourseTestCase(TestCase):

    def setUp(self):
        self.courses_django = mommy.make(
            'courses.Course', name='Python na web com Django', _quantity=5
        )
        self.courses_dev = mommy.make(
            'courses.Course', name='Python para Devs', _quantity=10
        )

    def tearDown(self):
        Course.objects.all().delete()

    def test_course_search(self):
        search = Course.objects.search('django')
        self.assertEqual(len(search), 5)
        search = Course.objects.search('dev')
        self.assertEqual(len(search), 10)
        search = Course.objects.search('python')
        self.assertEqual(len(search), 15)
