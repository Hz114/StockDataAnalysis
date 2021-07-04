#LoserStock.py

from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd
import os
import http.server
os.environ.setdefault("DJANGO_SETTINGS_MODULE","StockDataAnalysisProject.settings")

import django
django.setup()

# LoserStock load

from StockDataAnalysisApp.models import LoserStock

def parseLoserStock():

    names = []
    symbols = []
    prices = []
    changes = []
    percentChanges = []
    marketCaps = []
    totalVolumes = []
    circulatingSupplys = []

    for i in range(0, 6):
        CryptoCurrenciesUrl = "https://finance.yahoo.com/losers?offset=" + str(i) + "&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;count=100"
        r = requests.get(CryptoCurrenciesUrl)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')

        for listing in soup.find_all('tr', attrs={'class': 'simpTblRow'}):
            for symbol in listing.find_all('td', attrs={'aria-label': 'Symbol'}):
                symbols.append(symbol.text)
            for name in listing.find_all('td', attrs={'aria-label': 'Name'}):
                names.append(name.text)
            for price in listing.find_all('td', attrs={'aria-label': 'Price (Intraday)'}):
                prices.append(price.find('span').text)
            for change in listing.find_all('td', attrs={'aria-label': 'Change'}):
                changes.append(change.text)
            for percentChange in listing.find_all('td', attrs={'aria-label': '% Change'}):
                percentChanges.append(percentChange.text)
            for marketCap in listing.find_all('td', attrs={'aria-label': 'Market Cap'}):
                marketCaps.append(marketCap.text)
            for totalVolume in listing.find_all('td', attrs={'aria-label': 'Avg Vol (3 month)'}):
                totalVolumes.append(totalVolume.text)
            for circulatingSupply in listing.find_all('td', attrs={'aria-label': 'Volume'}):
                circulatingSupplys.append(circulatingSupply.text)

    StockData = {}
    StockData = {"Symbols": symbols, "Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges, "Market Cap": marketCaps, "Average Volume": totalVolumes, "Volume": circulatingSupplys}
    df = pd.DataFrame.from_dict(StockData, orient='index')
    df = df.transpose()
    StockDataList = df.values.tolist()

    # print(StockData)

    return StockDataList

if __name__=='__main__':

    StockDatalist = parseLoserStock()

    for i in range(len(StockDatalist)):
        LoserStock(Symbols=StockDatalist[i][0],Names=StockDatalist[i][1],Prices=StockDatalist[i][2],Changes=StockDatalist[i][3],PercentageChanges=StockDatalist[i][4],MarketCap=StockDatalist[i][5],AverageVolume=StockDatalist[i][6],Volume=StockDatalist[i][7]).save()



