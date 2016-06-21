from django.test import TestCase, Client

from django.core.urlresolvers import resolve, reverse_lazy
from django.contrib.auth.models import User


class UserAuthViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('mirabel2',
                                             'mirabel.ekwenugo@andela.com',
                                             '1234')

    def test_view_homepage(self):
        """Test that user request for homepage binds to a view class called `HomeView`.
        """

        response = resolve('/')
        self.assertEquals(response.func.__name__, 'HomeView')

    def test_user_post_signin(self):
        """Test that user post to google signin route has a session
        """
        data = {'email': 'mirabel.ekwenugo@andela.com', 'password': '1234'}
        response = self.client.post('/accounts/google/login', data)
        self.assertEquals(response.status_code, 301)

    def test_user_signout(self):

        response = self.client.get(reverse_lazy('user_logout'))
        self.assertEquals(response.status_code, 302)
