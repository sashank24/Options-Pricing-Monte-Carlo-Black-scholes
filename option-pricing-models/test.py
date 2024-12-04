from option_pricing import Ticker

data = Ticker.get_historical_data('AAPL')
if data is None:
    print("Failed to fetch data.")
else:
    print(data.head())
