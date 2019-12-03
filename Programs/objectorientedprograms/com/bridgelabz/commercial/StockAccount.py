import json

commercial = {'commercial data': []}
commercial["commercial data"].append({
    "company name": "tcs",
    "company shares": 150,
    "share per price": 100
})
commercial["commercial data"].append({
    "company name": "amazon",
    "company shares": 200,
    "share per price": 150
})
commercial["commercial data"].append({
    "company name": "mphasis",
    "company shares": 100,
    "share per price": 50
})
with open("commercial.json", "w") as out_file:
    json.dump(commercial, out_file, indent=4, sort_keys=True)

user = {"user details": []}
user["user details"].append({
    "customer name": "prem",
    "customer balance": 10000,
    "number of share": 0
}),
user["user details"].append({
    "customer name": "akash",
    "customer balance": 20000,
    "number of share": 0
}),
user["user details"].append({
    "customer name": "shubham",
    "customer balance": 30000,
    "number of share": 0
})
with open("user.json", "w")as out_file:
    json.dump(user, out_file, indent=4, )


class stockAccount:

    def buy(self, buying_amount, symbol):
        i = -1
        with open("commercial.json")as readfile:
            data_stock = json.load(readfile)

            # company_name = input("Which Company shares you have to Purchase..???")
            for value in data_stock['commercial data']:
                lst_comp_name = value["company name"]
                i = i + 1
                if symbol == lst_comp_name:
                    print(lst_comp_name)
                    print(i)
                    # print(value["company name"])
                    share_num = int(input("How many shares you want to purchase..??"))
                    shares_price = data_stock["commercial data"][0]["share per price"] * share_num
                    with open("commercial.json", "w") as update_file:
                        data_stock["commercial data"][i] = {
                            "company name": lst_comp_name,
                            "company shares": data_stock["commercial data"][i]["company shares"] - share_num,
                            "share per price": 100
                        }
                        json.dump(data_stock, update_file, indent=4, sort_keys=True)
                    break
        with open("user.json")as readfile:
            data_customer = json.load(readfile)
            for value in data_customer['user details']:
                lst_customer_amount = value["customer balance"]
                i = i + 1
                if buying_amount == lst_customer_amount:
                    print(lst_customer_amount)
                    print(i)
                    # print(value["company name"])
                    # share_num = int(input("How many shares you want to purchase..??"))
                    shares_price = data_stock["commercial data"][0]["share per price"] * share_num
                    with open("user.json", "w") as update1_file:
                        data_customer["user details"][i] = {
                            "customer name": "prem",
                            "customer balance": data_customer["user details"][i]["customer balance"] - shares_price,
                            "number of share": 0
                        }
                        json.dump(data_customer, update1_file, indent=4, sort_keys=True)

    def add_user(self):
        json_data = open('user.json', 'r')
        data_customer = json.load(json_data)
        username = input("Enter Name:-")
        for value in data_customer['user details']:
            # print(type(username))
            # print(type(value["customer name"]))
            if username not in (value['customer name']):
                balance = input("Enter the  Balance For New buyer:- ")
                # username = data_customer["user details"][0]["customer name"]
                # balance = data_customer["user details"][0]["customer balance"]
                with open("user.json", "w") as update1_file:
                    data_customer["user details"].append({
                        "customer name": username,
                        "customer balance": balance,
                        "number of share": 0
                    })
                    json.dump(data_customer, update1_file, indent=4, sort_keys=True)
                break
            else:
                print("This is Existing User")
            return False

    def add_company(self):
        json_data = open('commercial.json', 'r')
        data_new_company = json.load(json_data)
        company_name = input("Enter Name of company:-")
        for value in data_new_company['commercial data']:
            print(company_name)
            print(value["company name"])
            if company_name not in (value['company name']):
                new_comp_share = input("Enter the Number of shares New company have:- ")
                rate_per_share = input("Enter amount per share company have:-")
                # username = data_customer["user details"][0]["customer name"]
                # balance = data_customer["user details"][0]["customer balance"]
                with open("user.json", "w") as change_file:
                    data_new_company["commercial data"].append({
                        "company name": company_name,
                        "company share": new_comp_share,
                        "share per price": rate_per_share
                    })
                    json.dump(data_new_company, change_file, indent=4, sort_keys=True)
                break
            else:
                print("This is Existing Company")
            return False


def main():
    my_stock_account = stockAccount()

    while True:
        try:
            while True:
                print("What's in your Mind...?????\n1.Buy a share\n2.sell a share\n3.Save Files\n4.Print Stats")
                choice = int(input("Enter your choice:-"))
                if choice > 5:
                    print("Enter choice should be less than 7")
                else:
                    if choice == 1:
                        # my_stock_account.add_user()
                        # my_stock_account.add_company()
                        buying_amount = int(input("Enter Buying amount:-"))
                        symbol = input("Enter company name whose share you have to buy:-")
                        my_stock_account.buy(buying_amount, symbol)
        except ValueError:
            print("sorry..!!Invalid Input")


if __name__ == '__main__':
    main()
