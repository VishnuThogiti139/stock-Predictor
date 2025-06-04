import yfinance as yf
import pandas as pd

def get_historical_data(symbol, years=5):
    period = f"{years}y"
    return yf.download(symbol, period=period, interval="1d")

def get_live_price(symbol):
    return yf.Ticker(symbol).history(period="1d")["Close"].iloc[-1]

def get_stock_name(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d")
        if hist.empty:
            return f"❌ Invalid symbol: {symbol}"
        return symbol  # Optional: fallback to company name from another source
    except Exception:
        return f"❌ Invalid symbol: {symbol}"
def is_valid_symbol(symbol):
    try:
        return not yf.Ticker(symbol).history(period="1d").empty
    except:
        return False
    
