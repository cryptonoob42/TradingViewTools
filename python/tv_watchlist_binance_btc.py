#!/usr/bin/python

import json

from common import load_data, convert_to_watchlist, BASE_CURRENCY

response = load_data('https://api.binance.com/api/v1/ticker/allPrices')
if response != '':
    prices = json.loads(response)
    symbols = []

    for price in prices:
        symbol = price['symbol']
        if symbol.endswith(BASE_CURRENCY):
            symbols.append('BINANCE:{0}'.format(symbol))

    convert_to_watchlist(symbols)
