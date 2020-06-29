from app import app, invalid_inputs
from unittest import TestCase
from forex_python.converter import CurrencyRates, CurrencyCodes

app.config['TESTING']=True
app.config['DEBUG_TB_INTERCEPT_HOSTS']=['dont-show-debug-toolbar']

class ForexTestCase(TestCase):
    """ """
    def test_start_page(self):
        """ Test start page displays"""
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Convert Currency</h1>', html)
            
    
    def test_forex(self):
        """ test forex functions are correct"""
        with app.test_client() as client:
            resp = client.get('/convert', query_string={"inMoney":"USD", "outMoney":"usd", "amount":"1"})
            self.assertIn(b'1.0', resp.data)
        
    def test_invalid_inputs(self):
        """ Ensure invalid inputs properly flags bad input"""
        with app.test_client() as client: 
            resp = client.get('/convert', query_string={"inMoney":"USC", "outMoney":"JPx", "amount":"1@"})

            self.assertIn(b'USC not valid currency abbreviation', resp.data)
            self.assertIn(b'JPX not valid currency abbreviation', resp.data)
            self.assertIn(b'Amount input contained invalid character', resp.data)   