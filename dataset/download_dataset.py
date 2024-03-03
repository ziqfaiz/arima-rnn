import requests
import pandas as pd
import yfinance as yf
import os

def download_timeseries(symbol):
    timeseries = yf.Ticker(symbol)
    hist = timeseries.history(period="10y")
    symbol = symbol.replace("/", "_")
    name= 'timeseries/'+symbol +'_timeseries.csv'
    hist.to_csv(name)

symbols= pd.read_csv('top500marketcap.csv')['Symbol']

for symbol in symbols:
    download_timeseries(symbol)

#download_timeseries('BRK')

