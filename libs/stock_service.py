import yfinance as yf

from libs.models import StockDB, StockModel


def get_one_stock_from_api(ticker: str) -> StockDB:
    stock_data = yf.Ticker(ticker)
    info = stock_data.get_info()
    stock_db = StockDB(ticker, info.get("longName"), info.get("currentPrice"), info.get("trailingEps"), info.get("trailingPE"))
    return stock_db


def get_one_stock(ticker: str) -> StockModel:
    stock_db = get_one_stock_from_api(ticker)
    stock_model = StockModel(stock_db, 0.05, 0.1, 10)
    return stock_model


