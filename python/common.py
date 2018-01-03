import urllib2

BASE_CURRENCY = 'BTC'


def load_data(url):
    response = ''
    try:
        result = urllib2.urlopen(url)
        code = result.getcode()
        if code == 200:
            response = result.read()
        else:
            print 'Error retrieving data from URL {0} : status {1} returned.'.format(url, code)
    except urllib2.URLError as error:
        print 'Error retrieving data: {0}'.format(error.reason)

    return response


def convert_to_watchlist(symbols):
    symbols.sort()
    print ','.join(symbols)
