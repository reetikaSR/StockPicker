import sys
from load_stock_file import CSV
from utilities import parse_date, calculate_mean_std, find_profit, select_stocks


def main():
    try:
        file_path = sys.argv[1]
        csv_obj = CSV(file_path)
        stock_list = csv_obj.stock_list
        resp = 'y'
        while resp.lower() == 'y':
            try:
                stock_name = input("Welcome Agent! Which stock you need to process? ")
                is_exact_match, prefixed_words = csv_obj.t.list_words(stock_name)
                stock_name = input_stock_name(prefixed_words, stock_name, is_exact_match)
                if stock_list.__contains__(stock_name):
                    print('Processing for ' + stock_name)
                    start_date = parse_date(input("From which date you want to start "))
                    end_date = parse_date(input("Till which date you want to analyze "))
                    selected_stocks = select_stocks(stock_list[stock_name], start_date, end_date)
                    mean_value, std = calculate_mean_std(selected_stocks)
                    buy_date, sell_date, profit = find_profit(selected_stocks)
                    print("Here is you result " + "Mean: " + str(mean_value) + ", Std: " + str(std) + ", Buy date: " +
                          str(buy_date) + ", Sell date: " + str(sell_date) + ", Profit: Rs. " + str(profit))
                else:
                    print("stock not found")
            except Exception as e:
                print("some error Occurred", e)
            resp = input("Do you want to continue? (y or n) ")
    except:
        print("could not process file")


def input_stock_name(prefixed_words, stock_name, is_exact_match):
    if not is_exact_match:
        if prefixed_words is not None:
            for word in prefixed_words:
                if_word = input("Oops! Do you mean " + word + "? y or n ")
                if if_word.lower() == 'y':
                    return word
    return stock_name


if __name__ == '__main__':
    main()
