from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self): #
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self): #
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): #
        # There a website you could quiz your general knowledge
        # All you have to do is choose true or false
        # Direct to the website
        self.browser.get('http://localhost:8000')

        self.assertIn('This is a quiz.', self.browser.title)

        # There are a question that it need to be answer
        # First question
        # Donald Trump was born in thailand?
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Donald Trump was born in thailand?', header_text)
        # The answer should be false

        self.fail('Finish the test!') #
        # She is invited to enter a to-do item straight away


if __name__ == '__main__': #
    unittest.main(warnings='ignore')
