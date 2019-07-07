from utilities import parse_date


class Stock:
    def __init__(self, stock_date, price):
        self.stock_date = parse_date(stock_date)
        self.price = float(price)

