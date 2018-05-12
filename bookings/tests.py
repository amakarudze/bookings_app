import datetime

from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'bookings/index.html')

    def test_can_send_POST_request(self):
        start_date = datetime.datetime(2018, 5, 20, 10, 0).strftime('%Y/%m/%d %H:%M')
        end_date = datetime.datetime(2018, 5, 20, 10, 30).strftime('%Y/%m/%d %H:%M')
        response = self.client.post('/', data={'booking_name': 'New Booking',
                                               'start_date': start_date,
                                               'end_date': end_date})
        self.assertIn('New Booking', response.content.decode())
        self.assertTemplateUsed(response, 'bookings/index.html')
