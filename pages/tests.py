from django.test import SimpleTestCase
from django.urls import reverse

class PagesTests(SimpleTestCase):

    def test_home_page_view_is_up(self):
        response = self.client.get("/pages/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_view_is_up(self):
        response = self.client.get("/pages/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_uses_correct_template(self):
        response = self.client.get("/pages/")
        self.assertTemplateUsed(response, "pages/index.html")
        self.assertTemplateUsed(response, "base.html")

    def test_about_page_view_uses_correct_template(self):
        response = self.client.get("/pages/about/")
        self.assertTemplateUsed(response, "pages/about.html")
        self.assertTemplateUsed(response, "base.html")

    def test_home_page_view_has_correct_content(self):
        response = self.client.get("/pages/")
        self.assertContains(response, "Welcome home.")

    def test_about_page_view_has_correct_content(self):
        response = self.client.get("/pages/about/")
        self.assertContains(response, "About the author blablabla.")

    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/index.html")

    def test_about_page_reverse_lookup(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/about.html")
