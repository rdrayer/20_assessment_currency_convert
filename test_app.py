from app import app
from unittest import TestCase

class CurrencyHomeTestCase(TestCase):
    def test_currency_home(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Currency Converter</h1>', html)

class CurrencyCodeTestCase(TestCase):
    def test_currency_code(self):
        with app.test_client() as client:
            res = client.get('/result')
            html = res.get_data(as_text=True)

            #print(res)
            #self.assertEqual(res.status_code, 200)
            #self.assertIn('<h2>The result is: $ 1</h2>', html)