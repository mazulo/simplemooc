from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from simplemooc.accounts.models import Professor
from simplemooc.courses.models import Course


class ContactCourseTestCase(TestCase):

    def setUp(self):
        self.professor = Professor.objects.create(
            username='mazulo',
            email='pmazulo@gmail.com',
            name='Patrick Mazulo',
        )
        self.course = Course.objects.create(
            name='Django',
            slug='django',
            professor=self.professor
        )

    def tearDown(self):
        self.course.delete()

    def test_contact_form_error(self):
        data = {'name': 'Fulano de Tal', 'email': '', 'message': ''}
        client = Client()
        path = reverse('courses:details', args=[self.course.slug])
        response = client.post(path, data)
        self.assertFormError(
            response,
            'form',
            'email',
            'Este campo é obrigatório.'
        )
        self.assertFormError(
            response,
            'form',
            'message',
            'Este campo é obrigatório.'
        )

    def test_contact_form_success(self):
        data = {
            'name': 'Fulano de Tal',
            'email': 'admin@admin.com',
            'message': 'Oi'
        }
        client = Client()
        path = reverse('courses:details', args=[self.course.slug])
        # response = client.post(path, data)
        client.post(path, data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [settings.CONTACT_EMAIL])
