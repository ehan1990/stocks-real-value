import yfinance as yf

from libs.models import StockDB, StockModel
from libs.mongo_service import MongoService
from libs.constants import COL_STOCKS


def get_one_stock_from_api(ticker: str) -> StockDB:
    stock_data = yf.Ticker(ticker)
    info = stock_data.get_info()
    stock_db = StockDB(ticker, info.get("longName"), info.get("currentPrice"), info.get("trailingEps"), info.get("trailingPE"))
    return stock_db


def get_one_stock(ticker: str) -> StockModel:
    q = {"ticker": ticker}
    res = MongoService.query(COL_STOCKS, search=q)
    if len(res) == 1:
        stock_db = StockDB.from_db(res[0])
    else:
        stock_db = get_one_stock_from_api(ticker)
        MongoService.insert(COL_STOCKS, stock_db.__dict__)
    stock_model = StockModel(stock_db, 0.05, 0.1, 10)
    return stock_model


