import yfinance as yf
import pandas as pd

msft = yf.Ticker("MSFT")

financials = msft.financials
# print(financials)

ticker_symbol = "aapl"

aapl_ticker = yf.Ticker(ticker_symbol)

financials_aapl = aapl_ticker.financials


sept092022 = financials_aapl.columns[1]

# print(f"Column Name: {sept092022}")
# print(financials_aapl[sept092022])


# Access the 10th row (Python uses 0-based indexing, so index 10 is the 11th row)
sept092022_row = financials_aapl.iloc[10]

# Print the row
print(sept092022_row)
