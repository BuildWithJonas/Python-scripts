import yfinance as yf
import pandas as pd

# Define your tickers here for easy modification
X_TICKER = "BTC-USD"
Y_TICKER = "FTM-USD"

# Fetch historical data
data = yf.download([X_TICKER, Y_TICKER], start="2020-08-01", end="2025-01-01", interval="1d")

# Check if 'Adj Close' exists, otherwise use 'Close'
if 'Adj Close' in data.columns:
    prices = data['Adj Close']
else:
    prices = data['Close']

# Calculate daily returns
returns = prices.pct_change().dropna()

# Calculate correlation ratio
correlation = returns.corr().loc[X_TICKER, Y_TICKER]

# Calculate beta (how much Y moves when X moves 1%)
beta = returns[Y_TICKER].std() / returns[X_TICKER].std() * correlation

# Output results
print(f"Correlation between {X_TICKER} and {Y_TICKER}: {correlation:.2f}")
print(f"Beta (how much {Y_TICKER} moves when {X_TICKER} moves 1%): {beta:.2f}")