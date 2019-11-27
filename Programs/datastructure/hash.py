from datastructure.Utility import linked_list, Node


def main():
    while True:
        try:
            f = open('hash', 'r')
            text = f.read()
            lst = text.split(" ")
            print(lst)
            my_objects = []
            my_temp = linked_list()
            for i in range(0, 11):
                my_objects.append(linked_list())

            for i in range(len(lst)):
                slot = int(lst[i]) % 11
                # print(slot)
                my_temp = my_objects[slot]
                my_temp.push(lst[i])

            for i in range(len(lst)):
                my_temp = my_objects[i]
                my_temp.display()
                print()
            while True:

                search = input("Enter a Number to search: ")
                key = int(search) % 11
                print("Remainder for Given Element is ", key)
                key = Node(search)
                # my_temp = my_objects[key]
                counter = my_temp.search(search)
                if counter == 1:
                    print("Data found")
                    my_temp.delete_node(search)
                    print("---------------------------------------------------------------------------")
                    my_temp.display()
                    print()
                else:
                    print("Data Not found")
                    my_temp.insert(key)
                    print("------------------------------------------------------------------------------")
                    my_temp.display()
                    print()

        except AttributeError:
            print("Sorry...!Invalid Input")

        except ValueError:
            print("Sorry...!Invalid Input")


if __name__ == '__main__':
    main()
