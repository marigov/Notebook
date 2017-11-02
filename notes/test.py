from django.contrib.auth.models import User
from django.test import RequestFactory
from django.test import TestCase
from .views import profile

class MVPTests(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def test_login(self):

        response = self.client.post('/login/', self.credentials, follow=True)

        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, "/")

    def test_no_login(self):
        self.wrongCredentials = {
            'username': 'test',
            'password': 'pass'}

        response = self.client.post('/login/', self.wrongCredentials, follow=False)

        self.assertFalse(response.context['user'].is_authenticated)
        self.assertTrue(response.status_code == 200)

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/profile/')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user

        # Test my_view() as if it were deployed at /customer/details
        response = profile(request)
        self.assertEqual(response.status_code, 200)
