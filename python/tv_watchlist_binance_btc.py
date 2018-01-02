#!/usr/bin/python

import json
import urllib2

try:
    result = urllib2.urlopen('https://api.binance.com/api/v1/ticker/allPrices')
    if result.getcode() == 200:
        prices = json.loads(result.read())

        bi_symbols = []
        for price in prices:
            symbol = price['symbol']
            if not symbol.endswith('BTC'):
                continue

            bi_symbols.append('BINANCE:' + symbol)

        bi_symbols.sort()
        print ','.join(bi_symbols)
    else:
        print 'Error retrieving symbols. HTTP result: ', result.getcode()
except urllib2.URLError:
    print 'Error retrieving symbols.'
