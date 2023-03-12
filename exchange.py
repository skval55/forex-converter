import requests
from currency_symbols import CurrencySymbols

url = 'https://api.exchangerate.host/latest'
response = requests.get(url)
rates = response.json()['rates']



def valid_request(convert_from, convert_to, amount):
    """checks if inputs received are valid request to make to api
    
    >>> valid_request('USD', 'UGX', '13')
    []
    
    >>> valid_request('USD', 'pop', '13')
    ['code: pop']
  
    >>> valid_request('pee', 'pop', '13s')
    ['amount', 'code: pee', 'code: pop']
    
    """

    invalid = []
    if not amount.isdigit():
        invalid.append('amount')
    for val in [convert_from, convert_to]:
        if not val in rates:
            invalid.append(f'code: {val}')
    return invalid

def find_symbol(currency):
    """gets currency symbol with currency code ex: USD.
    if no symbol default to '$"

    >>> find_symbol('USD')
    '$'
   
    >>> find_symbol('UGX')
    'USh'
   
    >>> find_symbol('GBP')
    '£'
   
    >>> find_symbol('no symbol')
    '$'

    """

    symbol=CurrencySymbols.get_symbol(currency)
    if symbol == None:
        symbol = '$'
    return symbol

def get_result(convert_from, convert_to, amount):
    """gets the conversion results from api

    >>> get_result('USD', 'USD', '1')
    1
    
    >>> get_result('invalid code', 'invalid code', 'invalid amount')
    
    """
    
    url = f'https://api.exchangerate.host/convert?from={convert_from}&to={convert_to}&amount={amount}&symbols={convert_to}&places=2'
    response = requests.get(url)
    data = response.json()
    return data['result']