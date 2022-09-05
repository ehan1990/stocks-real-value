
import click
import json

from libs import stock_service
from libs.constants import DB_NAME, COL_STOCKS
from libs.mongo_service import MongoService


@click.group(name="api")
def api_cmd():
    pass


@api_cmd.group(name="stock")
def stock_cmd():
    pass


@stock_cmd.command(name="add")
@click.option('--ticker', required=True)
def add_stock(ticker):
    pass


@stock_cmd.command(name="ls")
def show_all_stocks():
    pass

