"""Import 10 years of stock prices for the chosen 6 stocks 
tech =[MSFT, GOOG]  energy=[XOM, SHEL] healthcare=[JNJ, AZN] auto=[TSLA,TM] finance=[HSBC,JPM] 
and save them in a csv."""

import pandas as pd
import yfinance as yf


def download_timeseries(symbol):
    timeseries = yf.Ticker(symbol)
    hist = timeseries.history(period="10y")
    symbol = symbol.replace("/", "_")
    # name = "timeseriesfinal/" + symbol + "_timeseries.csv"
    hist.to_csv(symbol + "_timeseries.csv")


symbols = ["MSFT", "GOOG", "XOM", "SHEL", "JNJ", "AZN", "TSLA", "TM", "HSBC", "JPM"]

for symbol in symbols:
    download_timeseries(symbol)
