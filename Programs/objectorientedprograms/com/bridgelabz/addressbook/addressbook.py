import json

address = {'address-data': []}
address["address-data"].append({
    "first-name": "prem",
    "last-name": "Chouhan",
    "address": "kamothe",
    "city": "mumbai",
    "state": "maharastra",
    "zip": 411048,
    "phone-number": 9850698567
})

with open("address.json", "w")as write_file:
    json.dump(address, write_file, indent=4, sort_keys=True)


class AddressBook:
    def addRecord(self):
        """
        In this Function You can add record by giveing some fields it will be updated in your json file
        No return value is given
        """
        firstName = input("Enter First name of New User;-")
        lastName = input("Enter last name with INITIAL letter should CAPITAL of New User;-")
        addressUser = input("Enter Address  of New User;-")
        city = input("Enter city of New User;-")
        state = input("Enter state  of New User;-")
        zipCode = int(input("Enter Zip code for New User;-"))
        phoneNumber = int(input("Enter Phone Number  of New User;-"))
        # while 1:
        #     print("Zip code should be of 6 digits")
        #
        #     if 0 > zipCode > 6:
        #         return 1
        #     else:
        #         return 0
        # while 1:
        #     print("Phone Number should be of 10 digits")
        #
        #     if 0 > zipCode > 6:
        #         return 0
        #     else:
        #         return 1

        with open('address.json', 'r') as feeds_json:
            data_json = json.load(feeds_json)
        with open('address.json', 'w') as feeds_json:
            data = {
                "first-name": firstName,
                "last-name": lastName,
                "address": addressUser,
                "city": city,
                "state": state,
                "zip": zipCode,
                "phone-number": phoneNumber
            }
            data_json["address-data"].append(data)
            json.dump(data_json, feeds_json, indent=4, sort_keys=True)

    def editRecord(self, name):
        """Here you can Edit your record by entering First name and it will the update details which
        you have to update
        No return value is given"""
        counterRecord = -1
        with open('address.json', 'r') as feeds_json:
            data_json = json.load(feeds_json)
            for value in data_json['address-data']:
                lst_comp_name = value['first-name']
                counterRecord = counterRecord + 1
                if name == lst_comp_name:
                    lastName = input("Enter last name with INITIAL letter should CAPITAL of New User;-")
                    addressUser = input("Enter Address  of New User;-")
                    city = input("Enter city of New User;-")
                    state = input("Enter state  of New User;-")
                    zipCode = int(input("Enter Zip code for New User;-"))
                    phoneNumber = int(input("Enter Phone Number  of New User;-"))
                    with open('address.json', 'w') as feeds_json:
                        data_json["address-data"][counterRecord] = {
                            "first-name": name,
                            "last-name": lastName,
                            "address": addressUser,
                            "city": city,
                            "state": state,
                            "zip": zipCode,
                            "phone-number": phoneNumber
                        }
                        json.dump(data_json, feeds_json, indent=4, sort_keys=True)
                else:
                    print("If Not found GO to Option 1 to Add Record")

    def deleteRecord(self, delName):
        """here you can delete a record just by entering first name of the existing record otherwise you  have to
         add a record and then delete it
         No return value given"""
        counterRecord = -1
        with open('address.json', 'r') as feeds_json:
            data_json = json.load(feeds_json)
            # delName = input("Enter First name of Person Whose Record is to be deleted:")
            for value in data_json['address-data']:
                lst_comp_name = value['first-name']
                counterRecord = counterRecord + 1
                print(data_json["address-data"][counterRecord])
                if delName == lst_comp_name:
                    del data_json["address-data"][counterRecord]
                    with open('address.json', 'w') as feeds_json:
                        json.dump(data_json, feeds_json, indent=4, sort_keys=True)

    def searchRecord(self, searchName):
        """
        here you can search by First name that can be searched if not found
        then you can add record in It
        No return value Given
        """
        counterRecord = -1
        with open('address.json', 'r') as feeds_json:
            data_json = json.load(feeds_json)
            for value in data_json['address-data']:
                lst_comp_name = value['first-name']
                counterRecord = counterRecord + 1
                if searchName == lst_comp_name:
                    see = int(input("Search Name is in File Want to Display Press 1"))
                    if see == 1:
                        print(data_json["address-data"][counterRecord])
                else:
                    print("Entered Name is not in File Go to Option 1 to Add")


def main():
    my_address_book = AddressBook()
    while True:
        try:
            while True:

                choice = int(
                    input("Enter what operation you have to perform in Address book:-\n1.Add Record\n2.Edit "
                          "Record\n3.Delete Record\n4.Search Record\n5.Quit Address book"))
                if choice == 1:
                    my_address_book.addRecord()

                if choice == 2:
                    updaName = input("Enter name Whose record you have to update")
                    my_address_book.editRecord(updaName)

                if choice == 3:
                    delName = input("Enter First name of Person Whose Record is to be deleted:")
                    my_address_book.deleteRecord(delName)

                if choice == 4:
                    searName = input("Enter First name of Person Whose Record is to be Searched:")
                    my_address_book.searchRecord(searName)

                if choice == 5:
                    print("you are Exit from Address book")
                    exit()
                    break
        except ValueError:
            print("Sorry...!!!Invalid Input")


if __name__ == '__main__':
    main()


