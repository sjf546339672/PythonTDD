from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import resolve
from .views import home_page


# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(1+1, 3)


class HomePageTest(TestCase):

    # def test_root_url_resolves_home_page_view(self):
    #     found = resolve("/")
    #     self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        respose = home_page(request)
        expect_html = render_to_string("home.html")
        self.assertEqual(respose.content.decode(), expect_html)
        # self.assertTrue(respose.content.startswith(b"<html>"))
        # self.assertIn(b"<title>ToDo</title>", respose.content)
        # self.assertTrue(respose.content.endswith(b"</html>"))
        # self.assertTrue(respose.content.strip().endswith(b"</html>"))
