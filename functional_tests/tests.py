from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from quiz.models import Question
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self): #
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self): #
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows_text = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows_text])

    def test_can_start_a_list_and_retrieve_it_later(self): #
        # There a website you could quiz your general knowledge
        # All you have to do is choose Yes or No
        # Direct to the website
        self.browser.get('http://localhost:8000')
        time.sleep(1)
        self.assertIn('This is a quiz.', self.browser.title)

        # People can add questions
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Any Question?', header_text)

        input_box = self.browser.find_element_by_id("id_new_question")
        input_box.send_keys("Donald Trump was born in Thailand?")
        self.browser.find_element_by_id("id_submit").click()
        time.sleep(2)

        # There are a question that it need to be answer
        # First question
        # Donald Trump was born in Thailand?
        self.check_for_row_in_list_table('Donald Trump was born in Thailand? Yes No Delete')

        # The people know that is false
        # So they chose to vote no
        vote = self.browser.find_element_by_name('vote_no')
        vote.click()
        
        # The result has been shown
        result = self.browser.find_element_by_tag_name('h2').text
        message = 'Yes 0 No 1'
        self.assertEqual( message, result)
        time.sleep(3)
        
        self.browser.find_element_by_id('back').click()
        time.sleep(3)
        # Of course this is just a test so we have to delete a question too
        self.browser.find_element_by_name('delete_question').click()
        time.sleep(3)

        self.fail('Finish the test!') #
        # She is invited to enter a to-do item straight away


if __name__ == '__main__': #
    unittest.main(warnings='ignore')
    