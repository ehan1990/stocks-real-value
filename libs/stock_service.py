import json
import yfinance as yf


class Stock:

    def __init__(self, ticker: str, name: str, current_price: float, eps: float, pe: float):
        self.ticker = ticker
        self.name = name
        self.current_price = current_price
        self.eps = eps
        self.pe = pe
        self.growth_rate = 0.05
        self.roi = 0.10
        self.eps_list = self.get_eps_list(self.eps, 10)
        self.future_prices = self.get_future_prices(self.pe, self.eps_list, self.roi, 10)

    def get_eps_list(self, eps: float, years: int):
        data = []
        for i in range(years):
            if i == 0:
                data.append(eps)
                continue
            next_eps = data[i-1] * (1 + self.growth_rate)
            next_eps = round(next_eps, 4)
            data.append(next_eps)
        return data

    def get_future_prices(self, pe: float, eps_list: list, roi: float, years: int):
        data = [0] * years
        for i in range(years-1, -1, -1):
            if i == years - 1:
                data[i] = pe * eps_list[i]
                data[i] = round(data[i], 2)
                continue
            data[i] = data[i+1] / (1 + roi)
            data[i] = round(data[i], 2)
        return data


def get_one_stock(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.get_info()
    stock = Stock(ticker, info.get("longName"), info.get("currentPrice"), info.get("trailingEps"), info.get("trailingPE"))
    print(json.dumps(stock.__dict__, indent=2))
    return stock


