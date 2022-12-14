
import click
import json

from libs import stock_service
from libs.constants import DB_NAME, COL_STOCKS
from libs.mongo_service import MongoService


@click.group(name="db")
def db_cmd():
    pass


@db_cmd.group(name="stock")
def stock_cmd():
    pass


@stock_cmd.command(name="add")
@click.option('--ticker', required=True)
def add_stock(ticker):
    stock_db = stock_service.get_one_stock_from_api(ticker)
    MongoService.insert(COL_STOCKS, stock_db.__dict__)


@stock_cmd.command(name="ls")
def show_all_stocks():
    data = MongoService.get_all(COL_STOCKS)
    print(json.dumps(data, indent=2))


@stock_cmd.command(name="del")
@click.option('--ticker', required=True)
def del_stock(ticker):
    stock_service.delete_one_stock(ticker)


@stock_cmd.command(name="delall")
def del_all_stock():
    stocks = MongoService.get_all(COL_STOCKS)
    for stock in stocks:
        ticker = stock.get("ticker")
        stock_service.delete_one_stock(ticker)
