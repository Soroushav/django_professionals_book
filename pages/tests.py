from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView


class UrlTest(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_url_by_address(self):
        #response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    def test_url_by_name(self):
        #response = self.client.get(reverse('home'))
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        #response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_currect_html(self):
        #response = self.client.get('/')
        self.assertContains(self.response, 'Home')
        self.assertNotContains(self.response, 'Home1')

    def test_home_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def about_page_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def about_page_contain_html(self):
        self.assertContains(self.response, 'About Page')

    def about_page_not_contain_html(self):
        self.assertNotContains(self.response, 'This is not')

    def about_page_view_used(self):
        view = resolve('about')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )