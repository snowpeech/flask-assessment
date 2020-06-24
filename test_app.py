from app import app, invalid_inputs
from unittest import TestCase
# from forex_python.converter import CurrencyRates, CurrencyCodes

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
            resp = client.get('/')
        
        # self.assertEqual(CurrencyRates.convert('USD','USD',1),1)
            self.assertEqual(c.get_symbol( 'USD'),"US$")

    # def test_invalid_inputs(self):
    #     """ Ensure invalid inputs properly flags bad input"""
    #     self.assertFalse(invalid_inputs("usd", "USD",10.0 ))
    #     self.assertFalse(invalid_inputs("usd", "USD","10" )) #no errors
        # self.assertTrue(invalid_inputs("USD!", "USD",10 ))
        # self.assertTrue(invalid_inputs("USD", "USA",10 ))
        # self.assertTrue(invalid_inputs("USD", "",10 ))

        # self.assertTrue(invalid_inputs("USD", "USD","0a" ))
        # self.assertTrue(invalid_inputs("USD", "USD","0!" ))
    

    # test routes for success and fail