from django.shortcuts import render
from .models import GainerStock

import os
import sys
sys.path.append(os.path.dirname(__file__))
import py.GainerStock as GS

# Create your views here.
def getGainerStock():
    StockDatalist = GS.parseGainerStock()

    for i in range(5):
        GainerStock(Symbols=StockDatalist[i][0], Names=StockDatalist[i][1], Prices=StockDatalist[i][2],
                    Changes=StockDatalist[i][3], PercentageChanges=StockDatalist[i][4], MarketCap=StockDatalist[i][5],
                    AverageVolume=StockDatalist[i][6], Volume=StockDatalist[i][7]).save()


def main(request):
    # 값 새로고침마다 업로드
    getGainerStock()

    gainerStocks = GainerStock.objects.all()
    gainerStocks = gainerStocks[len(gainerStocks)-5:len(gainerStocks)]

    return render(request, 'main.html', {'gainerStocks':gainerStocks})

