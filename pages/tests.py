from django.test import SimpleTestCase
from django.urls import reverse
class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
    def test_template_content(self): # new
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200) 
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200)
    def test_template_name_correct(self): # Test template name is correct with the templates
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
    def test_template_content(self): # new
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")
"""If you see an error such as AssertionError: 301 != 200 it’s
likely you forgot to add the trailing slash to "/about" above.The web browser knows to automatically add a slash if it’s
not provided, but that causes a 301 redirect, not a 200
success response!"""
# Create your tests here.
