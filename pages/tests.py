from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_content(self):
        response = self.client.get(reverse('home'))
        # print(response.content)
        self.assertContains(response, '<h1>Homepage</h1>')
        self.assertContains(response, 'Minus, excepturi')
        self.assertIn(b'<h1>Homepage</h1>', response.content)
        
class AboutPageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')

    def test_template_content(self):
        response = self.client.get(reverse('about'))
        # print(response.content)
        self.assertContains(response, '<h1>About</h1>')
        # self.assertIn(b'<h1>About</h1>', response.content)

    