import yfinance as yf

ticker = yf.Ticker("CW8.PA")

print(ticker.fast_info)

data = ticker.history(period="5d")

print(data)
