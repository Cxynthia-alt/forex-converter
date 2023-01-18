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

    try:
        if CurrencyConverter.validate(source_currency) is not True:
            flash(CurrencyConverter.validate(source_currency), 'error')
            redirect('/')
        if type(CurrencyConverter.validate(target_currency)) == 'str':
            flash(CurrencyConverter.validate(target_currency), 'error')
            redirect('/')
        convert_amount = f"{CurrencyConverter.convert(source_currency, target_currency, amount):.2f}"
        flash(f'The result is {target_symbol} {convert_amount}', 'success')
        return render_template('index.html')
    except RatesNotAvailableError:
        flash('There\'s no valid rate', 'error')
