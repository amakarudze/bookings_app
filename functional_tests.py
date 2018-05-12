import unittest
import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewBookingTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_new_booking(self):
        # Edith has heard about a cool new online booking app for the boardroom
        # at her workplace. She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention book boardroom
        self.assertIn('Book Boardroom', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Book Boardroom', header_text)

        # She is invited to enter a booking item straight away
        # She is first asked to select the subject of her meeting.
        inputbox = self.browser.find_element_by_id('id_new_booking')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter booking name'
                         )

        # She types in "Meeting with Dan from B2C."
        inputbox.send_keys('Meeting with Dan from B2C.')

        # Next she is prompted to enter the start date of her meeting.
        inputbox2 = self.browser.find_element_by_id('id_start_date')
        self.assertEqual(
            inputbox2.get_attribute('placeholder'),
            'Start date/time'
        )
        # She enters the start date "19/05/2018" and time "9 am".
        inputbox2.send_keys(datetime.datetime(2018, 5, 19, 9, 0, 0))

        # Next, she's asked to enter the end time of her meeting.
        inputbox3 = self.browser.find_element_by_id('id_end_date')
        self.assertEqual(
            inputbox3.get_attribute('placeholder'),
            'End date/time'
        )

        # She enters a end time of "10am" on the same day.
        # The meeting is only 1 hour long
        inputbox3.send_keys(datetime.datetime(2018, 5, 19, 10, 0, 0))

        # When she hits enter, the page updates, and now the page lists
        # "9am - 10am: Meeting with Dan from B2C" as a booking in a booking list
        inputbox3.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_booking_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == 'Meeting with Dan from B2C' for row in rows))

        # There is still a form inviting her to add another booking. She
        # enters "12 - 1: Appraisal Meeting with Marketing Team" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her booking list is still there.

        # Satisfied, she goes back to sleep
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
