#!/usr/bin/python

import json

from common import load_data, convert_to_watchlist, BASE_CURRENCY

response = load_data('https://bittrex.com/api/v1.1/public/getmarkets')
if response != '':
    markets = json.loads(response)
    if markets['success'] != True:
        print 'Markets were retrieved, but the success flag is false.'
        pass

    tv_symbols = []
    for market in markets['result']:
        if market['BaseCurrency'] == BASE_CURRENCY:
            tv_symbols.append('BITTREX:{0}{1}'.format(market['MarketCurrency'], BASE_CURRENCY))

    convert_to_watchlist(tv_symbols)
