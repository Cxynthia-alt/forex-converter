from flask import Flask, request, render_template, redirect, flash, session, jsonify
from forex_python.converter import CurrencyCodes, CurrencyRates
from flask_debugtoolbar import DebugToolbarExtension

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
    amount = int(request.form["amount"])

    if (len(target_currency) != 3 or target_currency is not target_currency.upper()):
        flash(f"Not a valid code: {target_currency}")
        return redirect("/")
    target_symbol = CurrencyCodes().get_symbol(target_currency)
    convert_amount = CurrencyRates(force_decimal=True).convert(
        source_currency, target_currency, amount)
    # import pdb
    # pdb.set_trace()
    return render_template("output.html", target_symbol=target_symbol, convert_amount=round(convert_amount, 2))
