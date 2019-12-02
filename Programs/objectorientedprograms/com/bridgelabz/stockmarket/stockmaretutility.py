import json


class stock:

    def add(self, share_name, share_price, share_num):
        with open('stock.json', 'r') as feeds_json:
            data_json = json.load(feeds_json)
        with open('stock.json', 'w') as feeds_json:
            data = {
                "share name": share_name,
                "share number": share_num,
                "share price": share_price,
                "total price": share_num * share_price
            }
            data_json["stock market"].append(data)
            json.dump(data_json, feeds_json, indent=4, sort_keys=True)
        return share_num * share_price


class stockPortfolio(stock):

    def total_stock_price(self):
        with open('stock.json') as readfile:
            data = json.load(readfile)
            lst = ["stock market"]
            total_stock = 0
            n = int(input("Enter N number of Stocks:-"))
            for outer_loop in range(n):
                share_name = input("Enter name of share:-")
                share_num = int(input("Enter number of shares:-"))
                share_price = int(input("Enter per price of share:-"))
                total = super().add(share_name, share_num, share_price)
                total_stock = total_stock + total
                for inner_loop in data[lst[outer_loop]]:
                    total = total + inner_loop["total price"]
        return total_stock, total