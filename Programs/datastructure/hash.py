from datastructure.Utility import linked_list, Node


def main():
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

        while True:
            for i in range(len(lst)):
                my_temp = my_objects[i]
                my_temp.display()
                print()
            search = input("Enter a Number to search: ")
            key = int(search) % 11
            print(key)
            key = Node(search)
            # my_temp = my_objects[key]
            counter = my_temp.search(search)
            if counter == 1:
                print("Data found")
                my_temp.deleteNode(search)
                print("---------------------------------------------------------------------------")
                for i in range(len(lst)):
                    my_temp = my_objects[i]
                    my_temp.display()
            else:
                print("Data Not found")
                my_temp.insert(key)
                print("------------------------------------------------------------------------------")
                for i in range(len(lst)):
                    my_temp = my_objects[i]
                    my_temp.display()

    except AttributeError:
        print("Sorry...!Invalid Input")

    except ValueError:
        print("Sorry...!Invalid Input")


if __name__ == '__main__':
    main()
