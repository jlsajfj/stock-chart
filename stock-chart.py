#!/usr/bin/python3.9
import sys
import datetime
import yfinance as yf
import matplotlib.pyplot as plt

def price(ticker: str, _period: str = 'max'):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=_period, debug=False)
    if hist.empty:
        raise Exception('No ticker info')
    openCloseData = hist[['Open', 'Close']]
    print(openCloseData)
    plt.plot(openCloseData)
    plt.show()

def main():
    price(sys.argv[1])

if __name__ == "__main__":
    main()