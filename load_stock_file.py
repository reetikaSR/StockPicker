import csv

from stock import Stock
from trie import Trie


class CSV:
    def __init__(self, path):
        self.stock_list = {}
        self.t = Trie()
        self.__load_csv(path)

    def __load_csv(self, file_path):
        with open(file_path, 'rt')as f:
            data = csv.reader(f)
            first = True
            for row in data:
                if not first:
                    stock_values = row[0].split('\t')
                    self.t.add_word(stock_values[0])
                    self.__add_stock(stock_values[0], Stock(stock_values[1], stock_values[2]))
                first = False
        self.__sort_stock_list()

    def __sort_stock_list(self):
        for stock in self.stock_list.keys():
            self.stock_list[stock].sort(key=lambda x: x.stock_date)

    def __add_stock(self, stock_name, stock):
        if not self.stock_list.__contains__(stock_name):
            self.stock_list[stock_name] = list()
        self.stock_list[stock_name].append(stock)