from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignUpView


class CustomUserTest(TestCase):
    def test_create_user(self):
        CustomUser = get_user_model()
        user = CustomUser.objects.create_user(
            username='hooman',
            password='testpass123',
            email='soroushav14@gmail.com',
        )
        self.assertEqual(user.username, 'hooman')
        self.assertEqual(user.email, 'soroushav14@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_superuser)


class CustomSignUpTests(TestCase):
    username = 'context'
    email = 'context@gmail.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_template_signup(self):
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'SignUp')
        self.assertEqual(self.response.status_code, 200)

    def test_signup_form(self):
        CustomUser = get_user_model()
        new_user = CustomUser.objects.create_user(username=self.username, email=self.email)
        self.assertEqual(CustomUser.objects.all().count(), 1)
        self.assertEqual(CustomUser.objects.all()[0].username, self.username)
        self.assertEqual(CustomUser.objects.all()[0].email, self.email)
