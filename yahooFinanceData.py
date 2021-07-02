import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np


from yahoo_finance import Share
import yfinance as yf

'''
import datetime
import pandas_datareader as pdr
from pandas_datareader import data
# 종목 타입에 따라 download url이 다름. 종목코드 뒤에 .KS .KQ등이 입력되어야해서 Download Link 구분 필요
stock_type = {
    'kospi': 'stockMkt',
    'kosdaq': 'kosdaqMkt'
}

# 회사명으로 주식 종목 코드를 획득할 수 있도록 하는 함수
def getCode(df, name):
    code = df.query("name=='{}'".format(name))['code'].to_string(index=False)

    # 위와같이 code명을 가져오면 앞에 공백이 붙어있는 상황이 발생하여 앞뒤로 sript() 하여 공백 제거
    code = code.strip()
    return code

# 종목 코드를 받아와 URL로 생성
def getDownloadStock(market_type=None):
    market_type_param = stock_type[market_type]
    download_link = 'http://kind.krx.co.kr/corpgeneral/corpList.do'
    download_link = download_link + '?method=download'
    download_link = download_link + '&marketType=' + market_type_param

    df = pd.read_html(download_link, header=0)[0]
    return df;

# kospi 종목코드 목록 다운로드 함수
def getDownloadKospi():
    df = getDownloadStock('kospi')
    df.종목코드 = df.종목코드.map('{:06d}.KS'.format)
    return df

# kosdaq 종목코드 목록 다운로드
def getDownloadKosdaq():
    df = getDownloadStock('kosdaq')
    df.종목코드 = df.종목코드.map('{:06d}.KQ'.format)
    return df

def getAllCode():
    # kospi, kosdaq 종목코드 각각 다운로드
    kospi_df = getDownloadKospi()
    kosdaq_df = getDownloadKosdaq()

    # data frame merge
    code_df = pd.concat([kospi_df, kosdaq_df])
    # data frame정리
    code_df = code_df[['회사명', '종목코드']]
    # data frame title 변경 '회사명' = name, 종목코드 = 'code'
    code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

    return code_df

def yahooFinanceData(name):
    code_df = getAllCode()
    code = getCode(code_df, name)
    # df = pdr.get_data_yahoo(code)

    # 수정 주기를 반영한 코드
    # 수정주가를 반영
    df = pdr.DataReader(code, adjust_price=True)
    df['Close'].plot(figsize=(10, 5))
    print(df['Close'].plot())

    # Open / High / Low / Close / Volume / Adj_Ratio
    df = data.YahooDailyReader('NWAU', '2010-07-04', '2016-07-08', adjust_price=True)

    #df = data.get_data_yahoo(code)
    print(df.read())
'''

if __name__ == '__main__':
    # yahooFinanceData('삼성전자')
    '''
    df = pdr.get_data_yahoo('NWAU')
    print(df['Close'].plot())
    '''
    #data = yf.download(['NWAU','MU', 'AMD'],start = '2019-01-01')
    #print(data)

    list = ["NWAU", "MU","AMD","SPY","AAPL"]

    for idx in range(len(list)):
        data = DataFrame(yf.download(list[idx], start="2021-06-01", end="2021-07-02"))
        print(data.columns) # 각 값
        print(data.index) # 날짜 데이터

        data['Adj Close'].plot()
        plt.xlabel("time")
        plt.ylabel("money")
        plt.show()

        #data['Adj Close'].plot().show()
        '''
        x = np.arange(1, 10)
        y = x * 5
        plt.plot(x, y)
        # print(plt.show())
        '''