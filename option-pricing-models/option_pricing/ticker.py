# Standard library imports
import datetime

# Third party imports
import requests_cache
import matplotlib.pyplot as plt
from pandas_datareader import data as wb


import yfinance as yf
import datetime

class Ticker:
    """Class for fetching data from Yahoo Finance."""

    @staticmethod
    def get_historical_data(ticker, start_date=None, end_date=None, cache_data=True, cache_days=1):
        """
        Fetches stock data from Yahoo Finance.

        Params:
        ticker: str, ticker symbol
        start_date: datetime.date or None, start date for historical data
        end_date: datetime.date or None, end date for historical data
        cache_data: bool, flag for caching fetched data (not used with yfinance)
        cache_days: int, number of days to cache the data (not used with yfinance)
        """
        try:
            # Set default date range if not provided
            if start_date is None:
                start_date = datetime.datetime.now() - datetime.timedelta(days=365)
            if end_date is None:
                end_date = datetime.datetime.now()

            # Fetch data using yfinance
            stock = yf.Ticker(ticker)
            data = stock.history(start=start_date, end=end_date)
            
            # Check if data is empty
            if data.empty:
                raise ValueError(f"No historical data found for ticker '{ticker}'.")

            return data

        except Exception as e:
            print(f"Error fetching data for ticker '{ticker}': {e}")
            return None

    @staticmethod
    def get_columns(data):
        if data is None:
            return None
        return [column for column in data.columns]

    @staticmethod
    def get_last_price(data, column_name):
        if data is None or column_name is None:
            return None
        if column_name not in Ticker.get_columns(data):
            return None
        return data[column_name].iloc[-1]

    @staticmethod
    def plot_data(data, ticker, column_name):
        try:
            if data is None:
                return
            data[column_name].plot()
            plt.ylabel(f'{column_name}')
            plt.xlabel('Date')
            plt.title(f'Historical data for {ticker} - {column_name}')
            plt.legend(loc='best')
            plt.show()
        except Exception as e:
            print(e)
            return
