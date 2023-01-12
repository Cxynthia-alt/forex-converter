from flask import Flask, request, render_template, redirect, flash, session, jsonify
from forex_python.converter import CurrencyCodes, CurrencyRates, RatesNotAvailableError
from flask_debugtoolbar import DebugToolbarExtension
from converter import CurrencyConverter

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def present_form():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    source_currency = request.form['source-currency']
    target_currency = request.form['target-currency']
    target_symbol = CurrencyConverter.get_symbol(target_currency)
    amount = int(request.form["amount"])
    # convert_amount = 0

    if CurrencyCodes().get_currency_name(source_currency) is None:
        flash('source currency not valid', 'error')
        redirect('/')
    if CurrencyCodes().get_currency_name(target_currency) is None:
        flash('target currency not valid', 'error')
        redirect('/')
    try:
        convert_amount = f"{CurrencyConverter.convert(source_currency, target_currency, amount):.2f}"
        flash('The result is here', 'success')
    except RatesNotAvailableError:
        flash('There\'s no valid rate', 'error')
    finally:
        return render_template("output.html", target_symbol=target_symbol, convert_amount=convert_amount)
