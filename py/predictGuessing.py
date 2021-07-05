from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import LSTM
import keras
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np


def make_dataset(data, label, window_size=20):
    feature_list = []
    label_list = []
    for i in range(len(data) - window_size):
        feature_list.append(np.array(data.iloc[i:i+window_size]))
        label_list.append(np.array(label.iloc[i+window_size]))
    return np.array(feature_list), np.array(label_list)


data_path = 'C:\\pythonProject4\\StockDataAnalysisProject\\StockDataAnalysisApp\\data\\'
model_path = 'C:\\pythonProject4\\StockDataAnalysisProject\\StockDataAnalysisApp\\data\\'
df_price = pd.read_csv(os.path.join(data_path, 'Samsung.csv'), encoding='utf8')
df_price.describe()
TEST_SIZE = 400 # 과거 000일전의 데이터부터 학습시킴
print(df_price.describe())

pd.to_datetime(df_price['일자'], format='%Y%m%d')
# 0      2020-01-07
# 1      2020-01-06
# 2      2020-01-03
# 3      2020-01-02
# 4      2019-12-30

df_price['일자'] = pd.to_datetime(df_price['일자'], format='%Y%m%d')
df_price['연도'] = df_price['일자'].dt.year
df_price['월'] = df_price['일자'].dt.month
df_price['일'] = df_price['일자'].dt.day

df = df_price.loc[df_price['연도'] >= 1990]

# plt.figure(figsize=(16, 9))
# sns.lineplot(y=df['종가'], x=df['일자'])
# plt.xlabel('time')
# plt.ylabel('price')
# plt.show()

# 데이터 셋을 만들기 위해 가공 중, 모든 데이터를 0 과 1사이로 매핑

scaler = MinMaxScaler()
scale_cols = ['시가', '고가', '저가', '종가', '거래량']
df_scaled = scaler.fit_transform(df[scale_cols])

df_scaled = pd.DataFrame(df_scaled)
df_scaled.columns = scale_cols

# print(df_scaled)

# 데이터셋 만들기

train = df_scaled[:-TEST_SIZE]
test = df_scaled[-TEST_SIZE:]

feature_cols = ['시가', '고가', '저가', '거래량']
label_cols = ['종가']

train_feature = train[feature_cols]
train_label = train[label_cols]

test_feature = test[feature_cols]
test_label = test[label_cols]

# train dataset
train_feature, train_label = make_dataset(train_feature, train_label, 50)

# train, validation set 생성
x_train, x_valid, y_train, y_valid = train_test_split(train_feature, train_label, test_size=0.4)

x_train.shape, x_valid.shape
# ((6086, 20, 4), (1522, 20, 4))

# test dataset (실제 예측 해볼 데이터)
test_feature, test_label = make_dataset(test_feature, test_label, 50)
test_feature.shape, test_label.shape
# ((180, 20, 4), (180, 1))

model = Sequential()
model.add(LSTM(16,
               input_shape=(train_feature.shape[1], train_feature.shape[2]),
               activation='relu',
               return_sequences=False)
          )
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')
early_stop = EarlyStopping(monitor='val_loss', patience=5)
filename = os.path.join(model_path, 'tmp_checkpoint.h5')
checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='auto')

history = model.fit(x_train, y_train,
                    epochs=200,
                    batch_size=16,
                    validation_data=(x_valid, y_valid),
                    callbacks=[early_stop, checkpoint])

model.load_weights(filename)
pred = model.predict(test_feature)
print(pred)

plt.figure(figsize=(12, 9))
plt.plot(test_label, label='actual')
plt.plot(pred, label='prediction')
plt.legend()
plt.show()
plt.savefig('test.png')