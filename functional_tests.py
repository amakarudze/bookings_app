import unittest
from selenium import webdriver


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
        assert 'Book Boardroom' in self.browser.title
        self.fail('Finish the test!')

# She is invited to enter a booking item straight away

# She picks a start time of "9am" in a select box (Edith has a
# meeting with a client that starts at 9am)

# She also picks an end time "10am" in a select box (Her meeting
# with the client ends at 10am )

# When she hits enter, the page updates, and now the page lists
# "9am - 10am: Meeting with Dan from B2C" as a booking in a booking list

# There is still a form inviting her to add another booking. She
# enters "12 - 1: Appraisal Meeting with Marketing Team" (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her booking list is still there.

# Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
