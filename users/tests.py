from django.test import TestCase
from django.urls import reverse
from .models import CustomUser
from django.contrib.auth import get_user
# Create your tests here.


class SignupTestCase(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse('users:signup'),
            data={
                'first_name': 'Shaxriyor',
                'username': 'shaxriyor008',
                'email': 'shaxriyor008@gmail.com',
                'password1': 'falonchi123',
                'password2': 'falonchi123',
            }
        )
        user = CustomUser.objects.get(username='shaxriyor008')
        self.assertEqual(user.first_name, 'Shaxriyor')
        self.assertEqual(user.email, 'shaxriyor008@gmail.com')
        self.assertTrue(user.check_password('falonchi123'))


        #profile test
        second_response = self.client.get("/users/profile/shaxriyor008")
        self.assertEqual(second_response.status_code, 200)

        # login
        self.client.login(username='shaxriyor008', password='falonchi123')

        #update
        third_response = self.client.post(
            reverse('users:update'),
            data={
                'username': 'shaxriyor0088',
                'first_name': 'Shaxriyor8',
                'last_name': 'Sharofov',
                'email': 'shaxriyor0088@gmail.com',
                'phone_number': '+998999999999',
                'tg_username': 'username',
            }
        )

        user = get_user(self.client)
        print(user.is_authenticated)
        self.assertEqual(third_response.status_code, 302)
        self.assertEqual(user.phone_number, '+998999999999')
        self.assertEqual(user.first_name, 'Shaxriyor8')
        self.assertNotEqual(user.first_name, 'Shaxriyor')


