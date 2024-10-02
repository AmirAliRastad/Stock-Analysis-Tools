import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def analyze_stock(stock_data):
    print("Stock Data Summary:")
    print(stock_data.describe())
    stock_data['Close'].plot(title='Stock Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

if __name__ == "__main__":
    # User Input
    ticker = input("Enter stock ticker (e.g., AAPL for Apple): ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Fetch and Analyze Stock Data
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    analyze_stock(stock_data)
