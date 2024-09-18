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


class Stonks_Portfolio:
    def __init__(self, stocks):
        # Initialize Ticker objects
        self.stocks = [yf.Ticker(stock) for stock in stocks]
        self.portfolio_value = 0  # Placeholder for portfolio value
        self.portfolio_risk = None  # Placeholder for future portfolio risk calculation

    def calculate_portfolio_value(self):
        """
        Calculate the total market value of the portfolio.
        """
        total_value = 0
        for stock in self.stocks:
            try:
                # Get the market price for each stock
                stock_price = stock.info.get['regularMarketPrice']
                print(f"{stock.ticker}: ${stock_price}")
                total_value += stock_price
            except Exception as e:
                print(f"Error getting price data for {stock.ticker}: {e}")
        self.portfolio_value = total_value
        return total_value


def display_portfolio(self):
    """
        Display the current portfolio value and details.
        """
    print(f"Total Portfolio Value: ${self.portfolio_value}")
    print("Individual Stocks in Portfolio:")
    for stock in self.stocks:
        print(f"- {stock.ticker}")
