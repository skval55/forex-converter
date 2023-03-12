import requests
from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from exchange import valid_request, find_symbol, get_result


app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
rates = response.json()['rates']


@app.route('/')
def homepage():
    """homepage runs home.html file"""
    return render_template('home.html')

@app.route('/convert', methods=['POST'])
def convert():
    """gets input values from form and calls upon api to do conversion"""
    amount = request.form['amount']
    convert_from = request.form['convert-from'].upper()
    convert_to = request.form['convert-to'].upper()

    invalid = valid_request(convert_from, convert_to, amount)
    if not len(invalid) == 0:
        for msg in invalid:
            flash(msg)
        return redirect('/')

    result = get_result(convert_from, convert_to, amount)  
    symbol = find_symbol(convert_to)

    return render_template('result.html', data=result, symbol=symbol)