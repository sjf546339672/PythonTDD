from django.http import HttpRequest
from django.template.loader import render_to_string
# from django.test import TestCase
from django.test import TestCase
from django.urls import resolve
from .views import home_page
from superlists.listsse.models import StudentModel
# class SmokeTest(TestCase):
#
#     def test_bad_maths(self):
#         self.assertEqual(1+1, 3)


# class HomPageTest(TestCase):

    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve("/home/")
    #     self.assertIn("home_page", str(found.func))

    # def test_home_page_returns_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     # print("---------", reponse.content)
    #     # self.assertTrue(reponse.content.startswith(b"<html>"))
    #     # self.assertIn(b"<title>To-Do lists</title>", reponse.content)
    #     # self.assertTrue(b"</html>")
    #     # expected_html = render_to_string("home.html")
    #     # print(expected_html)
    #     # print("====================")
    #     # print(reponse.content.decode("utf-8"))
    #     self.assertIn('A new list item', response.content.decode())
    #     expected_html = render_to_string('home.html',
    #                                      {'new_item_text': 'A new list item'})
    #     self.assertEqual(response.content.decode("utf-8"), expected_html)

    # def test_home_page_can_save_a_POST_request(self):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['item_text'] = 'A new list item'
    #     response = home_page(request)
    #     self.assertEqual(ItemModel.objects.count(), 1)
    #     new_item = ItemModel.objects.first()
    #     self.assertEqual(new_item.text, 'A new list item')
    #     self.assertIn('A new list item', response.content.decode())
    #     expected_html = render_to_string('home.html',
    #                                      {'new_item_text':  'A new list item'})
    #     self.assertEqual(response.content.decode(), expected_html)


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        print("11111111111111111111111111")
        print("----------------{}".format(StudentModel.objects.count()))
        self.assertEqual(StudentModel.objects.count(), 2)
        # first_item = ItemModel()
        # first_item.text = 'The first (ever) list item'
        # first_item.save()
        #
        # second_item = ItemModel()
        # second_item.text = 'Item the second'
        # second_item.save()
        #
        # saved_items = ItemModel.objects.all()
        # self.assertEqual(saved_items.count(), 2)
        #
        # first_saved_item = saved_items[0]
        # second_saved_item = saved_items[1]
        # self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        # self.assertEqual(second_saved_item.text, 'Item the second')



