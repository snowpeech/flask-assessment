from flask import Flask, flash,request, render_template, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config["SECRET_KEY"] = "secrets"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

r = CurrencyRates()
c = CurrencyCodes()

currency_abv={'IDR','BGN','ILS','GBP','DKK','CAD','JPY','HUF','RON','MYR','SEK','SGD','HKD','AUD','CHF','KRW','CNY','TRY','HRK','NZD','THB','EUR','NOK','RUB','INR','MXN','CZK','BRL','PLN','PHP','ZAR','USD'}

@app.route('/')
def start_page():
    """Home Page"""
    return render_template("base.html")

@app.route('/convert')
def convert_page():
    """this page will the receive inputs, get converted figure and redirect"""
    in_curr=request.args['inMoney'].upper()
    out_curr=request.args['outMoney'].upper()
    amt=request.args['amount']

    if invalid_inputs(in_curr,out_curr,amt):
        return render_template("base.html")
    
    else:
        amt=round(float(amt),2)
        converted = round(r.convert(in_curr,out_curr,amt),2)
        
        things={"insym": c.get_symbol(in_curr),"inamt":"{:.2f}".format(amt),"converted":converted, "symbol":c.get_symbol(out_curr)}
        
        return render_template("base.html", things=things)

def invalid_inputs(in_curr, out_curr, amt):
    """validates inputs"""
    errs=False

    try:
        amt=float(amt)
    except ValueError:
        errs=True
        flash("Amount input contained invalid character", "error")

    if in_curr not in currency_abv:
        errs=True
        flash(f"{in_curr} not valid currency abbreviation", "error")

    if out_curr not in currency_abv:
        errs=True
        flash(f"{out_curr} not valid currency abbreviation", "error")

    return errs
