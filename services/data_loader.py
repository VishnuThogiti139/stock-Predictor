import yfinance as yf
import pandas as pd

def get_historical_data(symbol, years=5):
    period = f"{years}y"
    return yf.download(symbol, period=period, interval="1d")

def get_live_price(symbol):
    return yf.Ticker(symbol).history(period="1d")["Close"].iloc[-1]

def get_stock_name(symbol):
    try:
        info = yf.Ticker(symbol).info
        return info.get("longName", symbol)
    except Exception:
        return f"❌ Invalid symbol: {symbol}"
    
