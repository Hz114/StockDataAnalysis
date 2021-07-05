import pandas as pd
import os

file_name = 'AAPL.csv'
data_path = 'C:\\venvs\\StockDataAnalysis-main\\StockDataAnalysisApp\\'
df_price = pd.read_csv(os.path.join(data_path, file_name), encoding='utf8')

AD_DF = df_price.drop(['Adj Close'], axis=1)
print(AD_DF.head())

# test = [i for i in range(0,10)]
# print(test)
# cool = test[-5:]
# print(cool)