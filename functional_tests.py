# coding: utf-8
import time

from selenium import webdriver
import unittest


class NewTest(unittest.TestCase):

    def setUp(self) -> None:
        self.brower = webdriver.Chrome()
        self.brower.implicitly_wait(3)

    def tearDown(self) -> None:
        self.brower.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.brower.get("http://127.0.0.1:9006/home/")
        time.sleep(10)


if __name__ == '__main__':
    unittest.main(warnings="ignore")
