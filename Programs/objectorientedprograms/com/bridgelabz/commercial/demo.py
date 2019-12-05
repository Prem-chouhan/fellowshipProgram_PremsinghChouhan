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
    "number of share": 10
}),
user["user details"].append({
    "customer name": "akash",
    "customer balance": 20000,
    "number of share": 10
}),
user["user details"].append({
    "customer name": "shubham",
    "customer balance": 30000,
    "number of share": 10
})
with open("user.json", "w")as out_file:
    json.dump(user, out_file, indent=4, )


def print():
    with open("commercial.json")as readfile:
        data_stock = json.load(readfile)
    with open("user.json")as readfile:
        data_customer = json.load(readfile)
        lst = ["user details"]
        # for value in data_customer['user details']:
        #     # print(data_customer['user details'])
        #     lst_customer_amount = value["company name"]
        #     print(lst_customer_amount)

        for i in range(len(lst)):
            print('{}.{}'.format(i + 1, lst[i]))

print()