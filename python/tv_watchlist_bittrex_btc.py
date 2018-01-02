#!/usr/bin/python

import json
import urllib2

try:
    result = urllib2.urlopen('https://bittrex.com/api/v1.1/public/getmarkets')
    if result.getcode() == 200:
        markets = json.loads(result.read())
        if markets['success'] != True:
            print 'Markets were retrieved, but the success flag is false.'
            pass

        tv_symbols = []
        for market in markets['result']:
            if market['BaseCurrency'] != 'BTC':
                continue

            tv_symbols.append('BITTREX:' + market['MarketCurrency'] + 'BTC')

        tv_symbols.sort()
        print ','.join(tv_symbols)
    else:
        print 'Error retrieving markets. HTTP result: ', result.getcode()
except urllib2.URLError:
    print 'Error retrieving markets.'
