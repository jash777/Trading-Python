import requests
import json

# Replace YOUR_API_KEY and YOUR_API_SECRET with your own Binance API key and secret
API_KEY = '*******************************'
API_SECRET = '******************************'

# Set up the request to the Binance API
url = 'https://api.binance.com/api/v3/klines'
params = {
    'symbol': 'GRTUSDT',  # Specify the symbol you want to retrieve data for
    'interval': '1h',  # Specify the time frame for the data
    'limit': 200  # Set the number of data points you want to retrieve
}

# Send the request and retrieve the data
response = requests.get(url, params=params)
data = response.json()

# Extract the close prices from the data
close_prices = [float(d[4]) for d in data]

# Calculate the moving averages
# You can adjust the number of periods and choose a different type of moving average
short_ma = sum(close_prices[-20:]) / 20
long_ma = sum(close_prices[-50:]) / 50

# Identify the support and resistance levels based on the moving averages and trendlines
if short_ma > long_ma:
    # The trend is up, so the support level is the long MA
    support = long_ma
    # The resistance level is the highest high in the recent trend
    resistance = max(close_prices[-20:])
else:
    # The trend is down, so the resistance level is the long MA
    resistance = long_ma
    # The support level is the lowest low in the recent trend
    support = min(close_prices[-20:])
print(f'Support: {support}, Resistance: {resistance}')
