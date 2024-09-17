import yfinance as yf
import pandas as pd

# msft = yf.Ticker("MSFT")

# get all stock info
# msft.info

# print(msft)
# download APPLE STOCK INFO
# data = yf.download("SPY AAPL", period="1mo", )

# print(data)

# print(data.info)
# print(data.shape)
# print(data['Volume'])

my_portfolio = [
    yf.Ticker("AAPL"),  # Apple
    yf.Ticker("MSFT"),  # Microsoft
    yf.Ticker("GLMD"),  # Galmed Pharmaceuticals
    yf.Ticker("ACN")    # Accenture
]


for stock in my_portfolio:
    try:
        # Some tickers might not have 'dividendRate', so we use .get() to avoid KeyErrors
        dividend_rate = stock.info.get(
            'dividendRate', 'No dividend data available')
        print(f"{stock.ticker}: {dividend_rate}")
    except Exception as e:
        print(f"Error retrieving data for {stock.ticker}: {e}")
