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

    def buy(self, username, buying_amount, company_name):
        """
        Here buyer with buy share and calculations are done of and
        buying amount  share will be Purchased and remaining amount will be addedto the balance of customer
        and number of shares will be also added
        No return values
        """
        counter_company = -1
        counter_user = -1
        with open("commercial.json")as readfile:
            data_stock = json.load(readfile)
        with open("user.json")as readfile:
            data_customer = json.load(readfile)
            for value in data_stock['commercial data']:
                lst_comp_name = value["company name"]
                counter_company = counter_company + 1
                if company_name == lst_comp_name:
                    # share_num = int(input("How many shares you want to purchase..??"))
                    # shares_price = data_stock["commercial data"][0]["share per price"] * share_num
                    share_user = buying_amount // data_stock["commercial data"][counter_company]["share per price"]
                    shares_price = share_user * data_stock["commercial data"][counter_company][
                        "share per price"]
                    remain_amount = buying_amount - shares_price
                    with open("commercial.json", "w") as update_file:
                        data_stock["commercial data"][counter_company] = {
                            "company name": company_name,
                            "company_shares": data_stock["commercial data"][counter_company][
                                                  "company shares"] - share_user,
                            "share per price": data_stock["commercial data"][counter_company][
                                "share per price"]
                        }
                        json.dump(data_stock, update_file, indent=4, sort_keys=True)
                    break
            for value in data_customer['user details']:
                lst_customer_amount = value["customer name"]
                counter_user = counter_user + 1
                if username == lst_customer_amount:
                    # shares_price = data_customer["commercial data"][0]["share per price"] * share_num
                    with open("user.json", "w") as update1_file:
                        data_customer["user details"][counter_user] = {
                            "customer name": username,
                            "customer balance": data_customer["user details"][counter_user][
                                                    "customer balance"] + remain_amount - buying_amount,
                            "number of share": data_customer["user details"][counter_user]["number of share"] + share_user
                        }
                        json.dump(data_customer, update1_file, indent=4, sort_keys=True)

    def sell(self, user_name, selling_amount, company_name):
        """
        Here  user will sell share to the company acording to there price
        and that amount will be added to the users account and Number of shares will be deducted
        from the user and added to company
        No return variables
        """
        counter_company = -1
        counter_user = -1
        with open("commercial.json")as readfile:
            data_stock = json.load(readfile)
        with open("user.json")as readfile:
            data_customer = json.load(readfile)
            for value in data_stock['commercial data']:
                lst_comp_name = value["company name"]
                counter_company = counter_company + 1
                if company_name == lst_comp_name:
                    # share_num = int(input("How many shares you want to purchase..??"))
                    # shares_price = data_stock["commercial data"][0]["share per price"] * share_num
                    share_user = selling_amount // data_stock["commercial data"][counter_company]["share per price"]
                    shares_price = share_user * data_stock["commercial data"][counter_company][
                        "share per price"]
                    remain_amount = selling_amount - shares_price
                    with open("commercial.json", "w") as update_file:
                        data_stock["commercial data"][counter_company] = {
                            "company name": company_name,
                            "company shares": data_stock["commercial data"][counter_company][
                                                  "company shares"] + share_user,
                            "share per price": data_stock["commercial data"][counter_company][
                                "share per price"]
                        }
                        json.dump(data_stock, update_file, indent=4, sort_keys=True)
                    break
            for value in data_customer['user details']:
                lst_customer_amount = value["customer name"]
                counter_user = counter_user + 1
                if user_name == lst_customer_amount:
                    # shares_price = data_customer["commercial data"][0]["share per price"] * share_num
                    with open("user.json", "w") as update1_file:
                        data_customer["user details"][counter_user] = {
                            "customer name": user_name,
                            "customer balance": data_customer["user details"][counter_user][
                                                    "customer balance"] + remain_amount + selling_amount,
                            "number of share": data_customer["user details"][counter_user][
                                                   "number of share"] - share_user
                        }
                        json.dump(data_customer, update1_file, indent=4, sort_keys=True)

    def check_user(self, username):
        """
        Here User validation will be done if the user is valid or Not
        """
        json_data = open('user.json', 'r')
        data_customer = json.load(json_data)
        for value in data_customer['user details']:
            if username == (value['customer name']):
                print("This is Existing User")
                return value["customer name"]

    def add_user(self, username):
        """
        If user is not Valid then the entry of new user will be done
        """
        json_data = open('user.json', 'r')
        data_customer = json.load(json_data)
        balance = int(input("Enter the  Balance For New buyer:- "))
        # username = data_customer["user details"][0]["customer name"]
        # balance = data_customer["user details"][0]["customer balance"]
        with open("user.json", "w") as update1_file:
            data_customer["user details"].append({
                "customer name": username,
                "customer balance": balance,
                "number of share": 0
            })
            json.dump(data_customer, update1_file, indent=4, sort_keys=True)

    def check_company(self, company_name):
        """here Validtion of company will be done if the company is present or not"""
        json_data = open('commercial.json', 'r')
        data_new_company = json.load(json_data)
        for value in data_new_company['commercial data']:
            if company_name == (value['company name']):
                print("This is Existing Company")
                # print(value["company name"])
                return value["company name"]

    def add_company(self, company_name):
        """Here if company is not present in then it will be added"""
        json_data = open('commercial.json', 'r')
        data_new_company = json.load(json_data)
        new_comp_share = int(input("Enter the Number of shares New company have:- "))
        rate_per_share = int(input("Enter amount per share company have:-"))
        # username = data_customer["user details"][0]["customer name"]
        # balance = data_customer["user details"][0]["customer balance"]
        with open("commercial.json", "w") as change_file:
            data_new_company["commercial data"].append({
                "company name": company_name,
                "company shares": new_comp_share,
                "share per price": rate_per_share
            })
            json.dump(data_new_company, change_file, indent=4, sort_keys=True)


def main():
    my_stock_account = stockAccount()
    while True:
        try:
            while True:
                print("What's in your Mind...?????\n1.Buy a share\n2.sell a share")
                choice = int(input("Enter your choice:-"))
                if choice > 5:
                    print("Enter choice should be less than 7")
                else:
                    if choice == 1:
                        company_name = input("Enter company name whose share you have to buy:-")
                        company_copy = my_stock_account.check_company(company_name)
                        if company_name != company_copy:
                            my_stock_account.add_company(company_name)
                        username = input("Enter Name of user who want to buy share: -")
                        user_copy = my_stock_account.check_user(username)
                        if username != user_copy:
                            my_stock_account.add_user(username)
                        buying_amount = int(input("Enter Buying amount:-"))
                        my_stock_account.buy(username, buying_amount, company_name)
                    if choice == 2:
                        company_name = input("Enter company name who want to buy share:-")
                        username = input("Enter Name of user who want to buy sell share: -")
                        amount = int(input("Enter selling amount:-"))
                        my_stock_account.sell(username, amount, company_name)

        except ValueError:
            print("sorry..!!Invalid Input")


if __name__ == '__main__':
    main()