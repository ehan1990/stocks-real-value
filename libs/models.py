
class StockDB:

    def __init__(self, ticker: str, name: str, current_price: float, eps: float, pe: float):
        self.ticker = ticker
        self.name = name
        self.current_price = current_price
        self.eps = eps
        self.pe = pe

    @staticmethod
    def from_db(data: dict):
        stock_db = StockDB(data["ticker"], data["name"], data["current_price"], data["eps"], data["pe"])
        return stock_db


class StockModel(StockDB):

    def __init__(self, stockDB: StockDB, growth_rate: float, roi: float, years: int):
        super().__init__(stockDB.ticker, stockDB.name, stockDB.current_price, stockDB.eps, stockDB.pe)
        self.growth_rate = growth_rate
        self.roi = roi
        self.years = years
        self.eps_list = self.get_eps_list()
        self.future_prices = self.get_future_prices()

    def get_eps_list(self) -> list:
        data = []
        for i in range(self.years):
            if i == 0:
                data.append(self.eps)
                continue
            next_eps = data[i - 1] * (1 + self.growth_rate)
            next_eps = round(next_eps, 4)
            data.append(next_eps)
        return data

    def get_future_prices(self) -> list:
        data = [0] * self.years
        for i in range(self.years - 1, -1, -1):
            if i == self.years - 1:
                data[i] = self.pe * self.eps_list[i]
                data[i] = round(data[i], 2)
                continue
            data[i] = data[i + 1] / (1 + self.roi)
            data[i] = round(data[i], 2)
        return data
