
import click
import json

from libs import stock_service
from libs.mongo_service import MongoService


@click.group(name="stock")
def stock_cmd():
    pass


@stock_cmd.command(name="add")
@click.option('--ticker', required=True)
def add_stock(ticker):
    stock_db = stock_service.get_one_stock_from_api(ticker)
    MongoService.insert("stocks", stock_db.__dict__)


@stock_cmd.command(name="ls")
def show_all_stocks():
    data = MongoService.get_all("stocks")
    print(json.dumps(data, indent=2))

