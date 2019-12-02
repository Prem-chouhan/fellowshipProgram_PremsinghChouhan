from objectorientedprograms.com.bridgelabz.stockmarket.stockmaretutility import stockPortfolio


def main():
    while True:
        try:
            while True:
                my_stock_portfolio = stockPortfolio()
                total_stock, total = my_stock_portfolio.total_stock_price()
                print(f"Total for entries of stock:- {total_stock}")
                print(f"Total Value for total stock is :-{total}")
        except ValueError:
            print("Sorry...!!Invalid input ")


if __name__ == '__main__':
    main()
