# coding: utf-8
import unittest
from selenium import webdriver

# brower = webdriver.Chrome()
# brower.get("http://localhost:8000")
# assert "Django" in brower.title


class NewVistorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.brower = webdriver.Chrome()
        self.brower.implicitly_wait(3)

    def tearDown(self) -> None:
        self.brower.quit()

    def test_can_start_a_llist_and_retrieve_it_later(self):
        self.brower.get("http://localhost:8000")
        self.assertIn("To-Do", self.brower.title)
        self.fail("Finish the test!")


if __name__ == '__main__':
    unittest.main(warnings="ignore")
