#!/usr/bin/python3.9
import sys
import datetime
import yfinance as yf
import matplotlib.pyplot as plt

def price(ticker: str, _period: str = '1mo', _interval: str = '1d'):
    stock = yf.Ticker(ticker)
    hist = stock.history(period = _period, debug = False, interval = _interval)
    if hist.empty:
        raise Exception('No ticker info')
    
    print(hist)
    openCloseData = hist[['Open', 'Close']]
    # print(openCloseData)
    fig, ax = plt.subplots()
    ax.plot(hist[['Open']], '-b', label='Open')
    ax.plot(hist[['Close']], '--r', label='Close')
    leg = ax.legend(frameon=False)
    plt.title(f"{ticker.upper()}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def main():
    if len(sys.argv) == 2:
        price(sys.argv[1], _period = '5d', _interval = '1h')
    if len(sys.argv) == 3:
        price(sys.argv[1], _period = sys.argv[2], _interval = '1d')
    if len(sys.argv) == 4:
        price(sys.argv[1], _period = sys.argv[2], _interval = sys.argv[3])

if __name__ == "__main__":
    main()