from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignUpTests(TestCase):
    username = 'user'
    password = 'password'

    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        user = get_user_model().objects.create_user(
            self.username, self.password
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].password, user.password)
