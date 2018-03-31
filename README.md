# TradingViewTools
Some scripts to automate things related to TradingView

# What you can find here
Look at the directory 'python' to see which scripts exist so far :)

To create a TradingView watchlist of the BTC markets at Bittrex,
just run tv_watchlist_bittrex_btc.py and redirect the output to
a txt file. Name the file the same as you want the new watchlist
to be named, for example BittrexBTC.txt. Go to TradingView, click
'Import Watchlist', upload the txt file and that's it.

To do the same for BTC markets at Binance, run tv_watchlist_binance_btc.py
and follow the same steps.

Have fun!

# Automated Builds
Each commit triggers a Travis build and there will soon be a cron job to create the watchlists on a weekly basis. The latest watchlists created by the automated builds are available at https://cryptonoob42.github.io/TradingViewTools/.

![Build Status](https://travis-ci.org/cryptonoob42/TradingViewTools.svg?branch=master)

