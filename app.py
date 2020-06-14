from flask import Flask, render_template,request
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
r = CurrencyRates()
# r.get_rate('USD', 'INR')    # same as get_rate('USD', 'INR')

# r.convert('USD', 'INR', 10)  # convert('USD', 'INR', 10)

c = CurrencyCodes()
# >>> c.get_symbol('GBP')
# u'\xa3'
# >>> print c.get_symbol('GBP')
# £
# >>> print c.get_symbol('EUR')
# €
