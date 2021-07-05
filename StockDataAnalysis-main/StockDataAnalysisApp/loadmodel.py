import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from keras.models import load_model


# 학습 and 테스트 데이터 셋 만들기
def make_dataset(data, label, window_size=20):
    feature_list = []
    label_list = []
    for i in range(len(data) - window_size):
        feature_list.append(np.array(data.iloc[i:i+window_size]))
        label_list.append(np.array(label.iloc[i+window_size]))
    return np.array(feature_list), np.array(label_list)


# 여기부터 ~~~~~
file_name = 'AAPL.csv'
model_name = 'test400_window50.h5'
TEST_SIZE = 400

# csv 파일, 모델 위치
data_path = 'C:\\venvs\\StockDataAnalysis-main\\StockDataAnalysisApp\\'
model_path = 'C:\\venvs\\StockDataAnalysis-main\\StockDataAnalysisApp\\'

Original = pd.read_csv(os.path.join(data_path, file_name), encoding='utf8')
df_price = Original.drop(['Adj Close'], axis=1)

# 데이터 셋을 만들기 위해 가공 중, 모든 데이터를 0 과 1사이로 매핑
scaler = MinMaxScaler()
scale_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
df_scaled = scaler.fit_transform(df_price[scale_cols])

df_scaled = pd.DataFrame(df_scaled)
df_scaled.columns = scale_cols
test = df_scaled[:TEST_SIZE]

feature_cols = ['Open', 'High', 'Low', 'Volume']
label_cols = ['Close']

# 테스트 데이터 피처 맞추기
test_feature = test[feature_cols]
test_label = test[label_cols]

# test dataset (실제 예측 해볼 데이터)
test_feature, test_label = make_dataset(test_feature, test_label, 50)
test_feature.shape, test_label.shape
# ((180, 20, 4), (180, 1))

# 테스트 셋 + 모델

model = load_model(model_name)
pred = model.predict(test_feature)

plt.figure(figsize=(12, 9))
plt.plot(test_label, label='actual')
plt.plot(pred, label='prediction')
plt.legend()
plt.savefig('test.png')
plt.show()