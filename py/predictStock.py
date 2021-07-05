from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import yfinance as yf

from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import os

def getFinanceData(symbol):
    data = DataFrame(yf.download(symbol))

    print(data.columns)  # 각 값
    print(data.index)  # 날짜 데이터

    #data['Adj Close'].plot()
    #plt.xlabel("time")
    #plt.ylabel("price")
    #plt.show()

    return data

def getDataset(data):
    df_price = data.drop(['Adj Close'], axis=1)
    print(df_price)

    scaler = MinMaxScaler()
    scale_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    df_scaled = scaler.fit_transform(df_price[scale_cols])
    df_scaled = pd.DataFrame(df_scaled)
    df_scaled.columns = scale_cols

    return df_scaled

# 학습 and 테스트 데이터 셋 만들기
def makeDataset(data, label, window_size=20):
    feature_list = []
    label_list = []
    for i in range(len(data) - window_size):
        feature_list.append(np.array(data.iloc[i:i+window_size]))
        label_list.append(np.array(label.iloc[i+window_size]))
    return np.array(feature_list), np.array(label_list)

def getPredict(dataset, TEST_SIZE):
    test = dataset[:TEST_SIZE]

    feature_cols = ['Open', 'High', 'Low', 'Volume']
    label_cols = ['Close']

    # 테스트 데이터 피처 맞추기
    test_feature = test[feature_cols]
    test_label = test[label_cols]

    # test dataset (실제 예측 해볼 데이터)
    test_feature, test_label = makeDataset(test_feature, test_label, 50)
    # test_feature.shape, test_label.shape
    # ((180, 20, 4), (180, 1))

    model_name = 'test400_window50.h5'

    model = load_model(model_name)
    pred = model.predict(test_feature)

    return test_label, pred

if __name__ == '__main__':
    data = getFinanceData('NOKPF')
    dataset = getDataset(data)
    actual, prediction = getPredict(dataset, 400)

    plt.plot(actual, label='actual')
    plt.plot(prediction, label='prediction')
    plt.show()