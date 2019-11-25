class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node

    def add_first(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            self.head = new_node
            self.head.next = temp_node
            del temp_node

    def add_position(self, new_node, pos):
        current_node = self.head
        current_position = 0
        while True:
            if current_position == pos:
                new_node.next = current_node
                prev_node.next = new_node
                break
            prev_node = current_node
            current_node = current_node.next
            current_position += 1

    def print_list(self):
        if self.head is None:
            print("List is Empty: ")
            return
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next

    def delete_end(self):
        last_node = self.head
        while last_node.next is not None:
            prev_node = last_node
            last_node = last_node.next
        prev_node.next = None

    def size(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            count += 1
        print("Size of a list is:", count)

    def is_empty(self):
        if self.head is None:
            print("List is Empty:")
        else:
            print("List is not Empty: ")

    def search(self, new_node):
        traverse_node = self.head
        while traverse_node is not None:
            if traverse_node.data == new_node.data:
                return 1
        traverse_node = traverse_node.next
        return 0

    def search_item(self, new_node):
        traverse_node = self.head
        while traverse_node is not None:
            value = 0
            if traverse_node.data == new_node.data:
                value = 1
                break
            else:
                traverse_node = traverse_node.next
        if value is 1:
            print("Data Found")
            return 1
        else:
            print("Data is not Found")
            return 0

    def delete_position(self, new_node):
        traverse_node = self.head
        prev_node = self.head
        if traverse_node.data == new_node.data:
            self.head = traverse_node.next
        else:
            while traverse_node.data != new_node.data:
                prev_node = traverse_node
                traverse_node = traverse_node.next
            prev_node.next = traverse_node.next

    def insert_ascending(self, new_node):
        # global
        prev_node = self.head
        traverse_node = self.head
        while traverse_node.data < new_node.data:
            prev_node = traverse_node
            traverse_node = traverse_node.next
        prev_node.next = new_node
        new_node.next = traverse_node

    def sort_ing(self, array1):
        length = len(array1)
        for outer_loop in range(length):
            for inner_loop in range(0, length - outer_loop - 1):
                if array1[inner_loop] > array1[inner_loop + 1]:
                    array1[inner_loop], array1[inner_loop + 1] = array1[inner_loop + 1], array1[inner_loop]


class Stack:

    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def is_empty(self):
        return self.elements == []

    def peek(self):
        if not self.is_empty():
            return self.elements[-1]

    def size(self):
        return len(self.elements)


class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def enqueue(self, element):
        self.elements.insert(0, element)

    def de_queue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def withdraw(self, balance):
        amount = int(input("Enter the Amount to withdraw:-"))
        if balance == 0:
            print("Insufficient balance in account")
        else:
            balance = balance - amount
            self.de_queue()
        return balance

    def deposit(self, balance):
        amount = int(input("Enter the amount to be Deposited:-"))
        balance = balance + amount
        self.de_queue()
        return balance


class NodeDequeue:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev_node = None
        self.last_node = None


class Dequeue:

    def __init__(self):
        self.head = None

    def add_front(self, new_node):
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        del temp_node

    # def add_rear(self, data):
    #     new_node = Node(data)
    #     cur_node = self.head
    #     while cur_node.next is not None:
    #         cur =cur_node.next
    #     cur.next = new_node

    def add_rear(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next
            last_node.next = new_node

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def size(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            count += 1
        return count

    def remove_rear(self):
        if self.head is not None:
            temp_node = self.head
            prev_node = self.head
            while temp_node.next is not None:
                prev_node = temp_node
                temp_node = temp_node.next
            prev_node.next = None
            return temp_node.data
        else:
            return None

    #     last_node = self.head
    #     prev_node = None
    #     while last_node.next is None:
    #         prev_node = last_node
    #         last_node = last_node.next
    #     prev_node.next = None

    def remove_front(self):
        if self.head is not None:
            prev_node = self.head
            self.head = self.head.next
            return prev_node.data
        else:
            return None

    def display(self):
        if self.head is None:
            print("List is Empty: ")
            return
        current_node = self.head
        print("Elements in List are:- ")
        while True:

            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next


def prime():
    lst = []
    for num in range(1, 100 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                lst.append(num)
    return lst


def is_anagram(p, q):
    while leng_th(p) == leng_th(q):
        # Testing sorted values equality
        if sorted(p) == sorted(q):
            return p, q
        return False


def leng_th(n):
    count = 0
    while n != 0:
        n /= 10
        count += 1
    return count
