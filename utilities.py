import dateparser
from statistics import mean, stdev


'''Selects the stocks list for the given range of dates '''
def select_stocks(stock_price_list, start_date, end_date):
    l = len(stock_price_list)
    start = find_stock_date(start_date, stock_price_list, l)
    end = find_stock_date(end_date, stock_price_list, l)
    return stock_price_list[start: end+1]


''' find the stock price for equal or less than the required date'''
def find_stock_date(date, stock_price_list, stock_length):
    first = 0
    last = stock_length - 1
    while first <= last:
        #print(first, last)
        mid = (first + last) // 2
        #print(stock_price_list[mid].stock_date)
        if stock_price_list[mid].stock_date == date:
            return mid
        elif stock_price_list[mid].stock_date < date:
            #print(mid, last, stock_price_list[mid + 1].stock_date)
            if mid == last or stock_price_list[mid + 1].stock_date > date:
                #print(mid)
                return mid
            first = mid + 1
        else:
            last = mid - 1
    return -1


'''using dateparser to handle all date formats'''
def parse_date(date):
    date_val = dateparser.parse(date)
    return date_val.date()


'''calculate mean and standard deviation here'''
def calculate_mean_std(selected_stocks):
    m = s = 0
    if selected_stocks is None or len(selected_stocks) == 0:
        return 0, 0
    prices = list(map(lambda x : x.price, selected_stocks))
    try:
        m = round(mean(prices), 3)
    except:
        m = 0
    try:
        s = round(stdev(prices), 3)
    except:
        s = 0
    return m, s


'''find the profit, buy date and sell date'''
def find_profit(selected_stocks):
    if selected_stocks is None or len(selected_stocks) == 0:
        return '', '', 0
    profit = 0
    current_min = selected_stocks[0].price
    buy_date = selected_stocks[0].stock_date
    sell_date = selected_stocks[0].stock_date
    for stock in selected_stocks:
        if stock.price - current_min > profit:
            profit = stock.price - current_min
            sell_date = stock.stock_date
        if stock.price < current_min:
            current_min = stock.price
            buy_date = stock.stock_date
    if profit <= 0:
        return '','',0
    return buy_date, sell_date, round(profit, 3)