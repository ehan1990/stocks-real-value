
import click
import json
import requests

from bs4 import BeautifulSoup


from libs import stock_service
from libs.constants import DB_NAME, COL_STOCKS
from libs.mongo_service import MongoService


class StockData:

    def __init__(self, rank, name, ticker, weight):
        self.rank = rank
        self.name = name
        self.ticker = ticker
        self.weight = weight


@click.group(name="web")
def web_cmd():
    pass


@web_cmd.command(name="update")
def update_sp500():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    res = requests.get("https://www.slickcharts.com/sp500", headers=headers)
    if res.status_code == 200:
        stock_data = []
        soup = BeautifulSoup(res.text, "lxml")
        table = soup.find('table', attrs={'class': 'table table-hover table-borderless table-sm'})
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]

            rank = int(cols[0])
            name = cols[1]
            ticker = cols[2].upper()
            weight = float(cols[3])
            stock_data.append(StockData(rank, name, ticker, weight).__dict__)

        with open("data/sp500.json", "w") as f:
            f.write(json.dumps(stock_data, indent=2))
        return
    raise Exception(f"status code {res.status_code}")
