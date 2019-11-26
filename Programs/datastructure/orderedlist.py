from datastructure.Utility import linked_list, Node


def main():
    try:
        f = open('order', 'r')
        text = f.read()
        my_list = linked_list()
        lst = []
        lst = text.split(" ")
        print(lst)
        my_list.sort_ing(lst)
        for loop in range(len(lst)):
            str = lst[loop]
            hold = Node(str)
            my_list.insert(hold)
        my_list.print_list()
        while True:
            search = input("Enter a Element in range of given number to insert: ")

            holder = Node(search)
            counter = my_list.search_item(holder)
            if counter == 1:
                my_list.delete_position(holder)
                my_list.print_list()
            else:
                my_list.insert_ascending(holder)
                my_list.print_list()
    except AttributeError:
        print("Sorry..!Number can only be Inserted Between Two Number")


if __name__ == '__main__':
    main()
