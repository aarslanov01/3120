'''
**Steps**
**1. Collecting Data**
- Choose five distinct equities or assets (oil, gold, bonds, currency pairs, bitcoins, etc…). Verify there is data available to import from Quandl, Alpha Vantage or Yahoo Finance.
- Import daily prices (adj closing or spot) for all five assets. Use 1/1/2022 as the start date and 12/31/2022 as the end date. Display the first 5 rows and the total count for each asset.
- Import daily prices for the S&P 500. Use 1/1/2022 as the start date and 12/31/2022 as the end date. Display the first 5 rows and the total count of the S&P.

**2. Processing Data**
- Calculate daily % change (adj closing or spot) for each of the asset and the S&P. Display the first 5 rows and the total count for each data set.
- Plot the daily % change (adj closing or spot) data using a bar graph for each asset.
- Calculate and display the mean, standard deviation, variance, min, and max for each set of data.

**3. Regression Analysis**
- Using scikit-learn, perform five linear regressions for each of the five assets against the S&P 500. Y should be % change S&P 500. X should be % change for each asset.
- For each regression, plot the samples and the linear model. Label the Y axis as S&P 500 and the X axis as each asset.
- Calculate and display the intercept, coefficient (slope), R2, and the Mean squared error.
- Which asset is highly correlated with the S&P 500 and which asset is the least correlated?

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import yfinance as yf

# Set start and end dates
start_date = '2022-01-01'
end_date = '2022-12-31'

# Define assets
assets = {
    'JPM': 'JPM',
    'ETH-USD': 'ETH',
    'BZ=F': 'Brent Crude Oil',
    'LQD': 'LQD',
    'GLD': 'GLD'
}

# Function to fetch data
def fetch_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)['Adj Close']
    return data

# Collect data
prices = {}
for ticker, asset in assets.items():
    prices[asset] = fetch_data(ticker, start_date, end_date)
    print(f'{asset} ({ticker}) - First 5 Rows:\n{prices[asset].head()}\nTotal Count: {len(prices[asset])}\n')

# Collect S&P 500 data
sp500 = fetch_data('^GSPC', start_date, end_date)
print(f'S&P 500 - First 5 Rows:\n{sp500.head()}\nTotal Count: {len(sp500)}\n')

# Calculate daily % change
daily_pct_change = {}
for asset, price_data in prices.items():
    daily_pct_change[asset] = price_data.pct_change().dropna()
    print(f'{asset} Daily % Change - First 5 Rows:\n{daily_pct_change[asset].head()}\nTotal Count: {len(daily_pct_change[asset])}\n')

# Calculate S&P 500 daily % change
sp500_daily_pct_change = sp500.pct_change().dropna()
print(f'S&P 500 Daily % Change - First 5 Rows:\n{sp500_daily_pct_change.head()}\nTotal Count: {len(sp500_daily_pct_change)}\n')

# Combine the daily_pct_change data for all assets and the S&P 500
all_daily_pct_changes = pd.concat([sp500_daily_pct_change.rename('S&P 500')] + [pct_change.rename(asset) for asset, pct_change in daily_pct_change.items()], axis=1)

# Drop rows with missing data
all_daily_pct_changes = all_daily_pct_changes.dropna()

# Update daily_pct_change and sp500_daily_pct_change
sp500_daily_pct_change = all_daily_pct_changes['S&P 500']
for asset in daily_pct_change:
    daily_pct_change[asset] = all_daily_pct_changes[asset]

# Plot daily % change
for asset, pct_change in daily_pct_change.items():
    plt.figure(figsize=(10, 6))
    ax = pct_change.plot(kind='bar', title=f'{asset} Daily % Change', xlabel='Date', ylabel='Percentage Change')

    # Reduce the number of x-axis tick labels
    ticks_to_show = np.arange(0, len(pct_change), len(pct_change) // 10)
    ax.set_xticks(ticks_to_show)
    ax.set_xticklabels([pct_change.index[i].strftime('%Y-%m-%d') for i in ticks_to_show], rotation=45)

    plt.show()


# Calculate descriptive statistics
for asset, pct_change in daily_pct_change.items():
    mean = pct_change.mean()
    std = pct_change.std()
    var = pct_change.var()
    minimum = pct_change.min()
    maximum = pct_change.max()
    
    print(f'{asset} Descriptive Statistics:\nMean: {mean}\nStandard Deviation: {std}\nVariance: {var}\nMin: {minimum}\nMax: {maximum}\n')

# Regression analysis
def perform_regression(x, y):
    x = x.values.reshape(-1, 1)
    y = y.values.reshape(-1, 1)
    model = LinearRegression().fit(x, y)
    y_pred = model.predict(x)
    return model, y_pred

correlations = {}
for asset, pct_change in daily_pct_change.items():
    model, y_pred = perform_regression(pct_change, sp500_daily_pct_change)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(pct_change, sp500_daily_pct_change, color='b')
    plt.plot(pct_change, y_pred, color='r')
    plt.xlabel(f'{asset} % Change')
    plt.ylabel('S&P 500 % Change')
    plt.title(f'Regression: {asset} vs S&P 500')
    plt.show()

    # Calculate and display metrics
    intercept = model.intercept_[0]
    slope = model.coef_[0][0]
    r2 = r2_score(sp500_daily_pct_change, y_pred)
    mse = mean_squared_error(sp500_daily_pct_change, y_pred)
    
    print(f'{asset} Regression Metrics:\nIntercept: {intercept}\nCoefficient (slope): {slope}\nR2: {r2}\nMean squared error: {mse}\n')

    # Store correlation
    correlations[asset] = r2

# Find the highest and lowest correlated assets
highest_corr_asset = max(correlations, key=correlations.get)
lowest_corr_asset = min(correlations, key=correlations.get)

print(f'The asset with the highest correlation with the S&P 500 is {highest_corr_asset} with a correlation of {correlations[highest_corr_asset]}.')
print(f'The asset with the lowest correlation with the S&P 500 is {lowest_corr_asset} with a correlation of {correlations[lowest_corr_asset]}.')

