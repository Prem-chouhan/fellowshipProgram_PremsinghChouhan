from datastructure.Utility import linked_list, Node


def main():
    f = open('read', 'r')
    text = f.read()
    my_list = linked_list()
    # lst = []
    lst = text.split(" ")
    print(lst)
    print("Strings in list are:-")
    for loop in range(len(lst)):
        elements = lst[loop]
        hold = Node(elements)
        my_list.insert(hold)
    my_list.print_list()
    while True:
        search = input("Enter a string to search: ")
        holder = Node(search)
        counter = my_list.search_item(holder)
        if counter == 1:
            my_list.delete_position(holder)
            my_list.print_list()
        else:
            my_list.insert(holder)
            my_list.print_list()


if __name__ == '__main__':
    main()
