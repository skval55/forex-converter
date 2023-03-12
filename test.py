from unittest import TestCase
from app import app
from flask import session

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class ExchangeCurrencyTestCase(TestCase):


    def test_home_page(self):
        """test home page connection"""
        with app.test_client() as client:

            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('Exchange Currency!', html)
   
    def test_valid_post_request(self):
        """test to see if valid request brings to results page"""
        with app.test_client() as client:

            response = client.post('/convert', data={'convert-from': 'USD',
                                                    'convert-to': 'USD',
                                                    'amount': '1'})
            html = response.get_data(as_text=True)

            self.assertIn('The result is $1', html)
            self.assertEqual(response.status_code, 200)

    def test_invalid_post_request(self):
        """test to see if invalid request redirects"""
        with app.test_client() as client:
            
            response = client.post('/convert', data={'convert-from': 'invalid',
                                                    'convert-to': 'poo',
                                                    'amount': 'not number'})

            self.assertEqual(response.status_code, 302)
