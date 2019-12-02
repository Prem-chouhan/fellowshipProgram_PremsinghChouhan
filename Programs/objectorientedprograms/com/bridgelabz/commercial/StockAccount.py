import json

# class stockAccount:
#     pass

commercial = {'commercial data': []}
commercial["commercial data"].append({
    "company name": "TCS",
    "company shares": 150,
    "share per price": 100
})
with open("commercial.json", "w") as out_file:
    json.dump(commercial, out_file, indent=4, sort_keys=True)

user = {"user details": []}
user["user details"].append({
    "customer name": "prem",
    "customer balance": 1000
})

with open("user.json", "w")as out_file:
    json.dump(user, out_file, indent=4, sort_keys=True)




def buy():
    with open("commercial.json", "r")as readfile:
        data_stock = json.load(readfile)
        # for key, value in commercial.items():
        #     print(data_stock["commercial data"][0]["company name"])
    with open("user.json", "r")as readfile:
        data_customer = json.load(readfile)

        # del user
        if data_stock["commercial data"][0]["company name"] == "TCS":
            if len("company shares") > 0:
                share_num = int(input("Enter number of shares to be purchased:-"))
                shares_price = data_stock["commercial data"][0]["share per price"] * share_num
                # print(shares_price)
                amount = data_customer["user details"][0]['customer balance'] - shares_price
                # print(amount)
                # print(data_stock["commercial data"][0]["company shares"] - share_num)
                # print(type(data_stock['commercial data'][0]["share per price"]))
    with open("commercial.json", "w") as update_file:
        data_stock["commercial data"][0] = {
            "company name": "TCS",
            "company shares": data_stock["commercial data"][0]["company shares"] - share_num,
            "share per price": 100
        }
        # print(data_stock["commercial data"][0]["company shares"] - share_num)
        json.dump(data_stock, update_file, indent=4, sort_keys=True)
    with open("user.json", "w") as update1_file:
        data_customer["user details"][0] = {
            "customer name": "prem",
            "customer balance": data_customer["user details"][0]["customer balance"] - shares_price
        }
        json.dump(data_customer, update1_file, indent=4, sort_keys=True)


def add_user():
    
    pass


def add_company():
    pass


def main():
    while True:
        try:
            while True:
                print("What's in your Mind...?????\n1.Buy a share\n2.sell a share\n3.Print Stats")
                choice = int(input("Enter your choice:-"))
                if choice > 7:
                    print("Enter choice should be less than 7")
                else:
                    if choice == 1:
                        buy()
        except ValueError:
            print("sorry..!!Invalid Input")


if __name__ == '__main__':
    main()
