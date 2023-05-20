import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

def process_data(df, price_col, time_col, lag):
    df['Lag.Price'] = df[price_col].shift(lag)
    return df

def build_model(df, price_col, time_col):
    model = sm.OLS(df[price_col], sm.add_constant(df[time_col]))
    output = model.fit()
    return output

def mape(df, price_col, predicted_col):
    df['APE'] = np.abs((df[price_col] - df[predicted_col]) / df[price_col])
    mape = np.mean(df['APE'] * 100)
    return round(mape, 2)

def linear_model_prediction(lagged_price, constant, coefficient):
    predicted_price = constant + coefficient * lagged_price
    return predicted_price

file_path = 'C:/Users/a.arslanov/Desktop/data1.xlsx'
df = load_data(file_path)

output = build_model(df, '  Price ($/barrel)  ', '  Time  ')
print(output.summary())

df = process_data(df, '  Price ($/barrel)  ', '  Time  ', 1)
df.to_excel('autoregressive2.xlsx', index=False)

df2 = df.loc[:, ['  Time  ', '  Price ($/barrel)  ']]
df2['  Price ($/barrel)  '] = np.log10(df2['  Price ($/barrel)  '])

output2 = build_model(df2, '  Price ($/barrel)  ', '  Time  ')
print(output2.summary())

df2 = process_data(df2, '  Price ($/barrel)  ', '  Time  ', 1)

df['predicted price'] = [15.705 + 1.666 * lp for lp in df['Lag.Price']]
print('MAPE model 1:', mape(df, '  Price ($/barrel)  ', 'predicted price'))

df2['predicted price'] = [1.283 + 0.020 * lp for lp in df2['Lag.Price']]
print('MAPE model 2:', mape(df2, '  Price ($/barrel)  ', 'predicted price'))

df3 = df2
df3['predicted price'] = [0.785 + 1.028 * lp for lp in df3['Lag.Price']]
print('MAPE model 3:', mape(df3, '  Price ($/barrel)  ', 'predicted price'))

lagged_price = 55.2
print('linear model prediction for the q2 2003:', linear_model_prediction(lagged_price, 15.455, 1.687))
