class Node:  # Creating a node class
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:  # creating a linkedlist class

    def __init__(self):
        self.head = None  # initializing head to None

    # This function is in LinkedList class
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)

        #  Make next of new Node as head
        new_node.next = self.head

        #  Move the head to point to new Node
        self.head = new_node

    # This Function is in Linked list class
    # Function to search a node
    def search(self, x):
        current = self.head
        while current is not None:  # traverse til l None
            if current.data is x:  # When data find return 1
                return 1
            current = current.next
        return 0

    # This Function is in Linked list class
    # Function to search a node
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
            print("Data Found  \nAfter Deletion:")
            return 1

        else:
            print("Data is NOT in the file")
            return 0

    # This Function is in Linked list class
    # Function to display a nodes
    def display(self):

        # Node current will point to head
        current = self.head

        if self.head is None:
            print("Slot is empty")
            return
        print("Nodes for slot is:", end="--------> ")

        while current is not None:
            # Prints each node by incrementing pointer
            print(current.data, end="------->")
            current = current.next

    # This Function is in Linked list class
    # Function to Insert a node
    def insert(self, new_node):

        if self.head is None:
            self.head = new_node  # Make head as new node

        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next  # Traverse till last node
            last_node.next = new_node  # Add node at the last

    # This Function is in Linked list class
    # Function to add at Start a node
    def add_first(self, new_node):
        if self.head is None:  # check if the node is present or not
            self.head = new_node

        else:
            temp_node = self.head  # Take a Temporary node and point it it as head
            self.head = new_node  # point new node to head
            self.head.next = temp_node  # point  head of next to new node
            del temp_node  # Delete a temp node

    # This Function is in Linked list class
    # Function to Add element at position a node
    def add_position(self, new_node, pos):
        current_node = self.head
        current_position = 0  # Take a counter to count
        while True:

            if current_position == pos:  # Matches the position
                new_node.next = current_node  # new node will point to current node
                prev_node.next = new_node  # previous node will point to new node
                break
            prev_node = current_node  # previous point to current node
            current_node = current_node.next  # pointing current node to Next node
            current_position += 1  # incrementing Counter

    # This Function is in Linked list class
    # Function to Print  a nodes
    def print_list(self):
        if self.head is None:
            print("List is Empty: ")
            return
        current_node = self.head
        while True:
            # print("After Deleting the Element")
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next

    # This Function is in Linked list class
    # Function to delete At end a node
    def delete_end(self):
        last_node = self.head

        while last_node.next is not None:
            prev_node = last_node
            last_node = last_node.next  # Traverse till last node
        prev_node.next = None  # Changing refrence to None

    # This Function is in Linked list class
    # Function to Size of node
    def size(self):
        count = 0  # Counter is Initialized
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next  # Traverse node till last
            count += 1  # Incrementing counter
        print("Size of a list is:", count)

    # This Function is in Linked list class
    # Function to know list is empty
    def is_empty(self):
        if self.head is None:  # See whether head is none
            print("List is Empty:")
        else:
            print("List is not Empty: ")

    # This Function is in Linked list class
    # Function to delete  a node
    def delete_node(self, key):
        """

            :param
            :return void
        """
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data is key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

            # if key was not present in linked list
        if temp is None:
            return

            # Unlink the node from linked list
        prev.next = temp.next

        temp = None

    # This Function is in Linked list class
    # Function to delete At position a node
    def delete_position(self, new_node):
        traverse_node = self.head
        prev_node = self.head

        if traverse_node.data == new_node.data:  # check if the new node and traverse node is same
            self.head = traverse_node.next  #
        else:

            while traverse_node.data != new_node.data:
                prev_node = traverse_node
                traverse_node = traverse_node.next  # traverse a node till the element
            prev_node.next = traverse_node.next

    # This Function is in Linked list class
    # Function to inserting nodes in Ascending order
    def insert_ascending(self, new_node):
        # global
        prev_node = self.head
        traverse_node = self.head

        while traverse_node.data < new_node.data:  # checking if the previous node is smaller than the next node
            prev_node = traverse_node
            traverse_node = traverse_node.next  # swapping the nodes

        prev_node.next = new_node
        new_node.next = traverse_node

    # This Function is in Linked list class
    # Function to  Sorting elements
    def sort_ing(self, array1):
        length = len(array1)
        for outer_loop in range(length):
            for inner_loop in range(0, length - outer_loop - 1):
                if array1[inner_loop] > array1[inner_loop + 1]:  # checking the number are greater than or less than
                    array1[inner_loop], array1[inner_loop + 1] = array1[inner_loop + 1], array1[inner_loop]
                    # Swapping numbers


class NodeDequeue:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev_node = None
        self.last_node = None


class Dequeue:  # class for Double Ended Queue

    def __init__(self):
        self.head = None

    # This Function is in Dequeue class
    # Function to  Add at front
    def add_front(self, new_node):
        temp_node = self.head  # Take a temp node and point it to head
        self.head = new_node  # give a link to new node as head
        self.head.next = temp_node  # Give a temp node to head of next
        del temp_node  # Delete temp node

    # This Function is in Dequeue class
    # Function to  add at end
    def add_rear(self, new_node):
        if self.head is None:
            self.head = new_node  # node is not present then give new node as head

        else:
            last_node = self.head

            while True:
                if last_node.next is None:
                    break
                last_node = last_node.next  # traverse till the last
            last_node.next = new_node  # Add a node at last

    # This Function is in Dequeue class
    # Function to see if dequeue is empty
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # This Function is in Dequeue class
    # Function to  check Size
    def size(self):
        count = 0  # initialize counter to 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next  # traverse till last of the nodes
            count += 1  # Increment counter
        return count

    # This Function is in Dequeue class
    # Function to  remove from last
    def remove_rear(self):

        if self.head is not None:
            temp_node = self.head
            prev_node = self.head

            while temp_node.next is not None:
                prev_node = temp_node
                temp_node = temp_node.next  # Traverse till last of the Dequeue
            prev_node.next = None  # point the previous node to  none
            return temp_node.data

        else:
            return None

    # This Function is in Dequeue class
    # Function to  Remove from front
    def remove_front(self):
        if self.head is not None:
            prev_node = self.head  # point previous node to head
            self.head = self.head.next  # point head to the next
            return prev_node.data
        else:
            return None

    # This Function is in Dequeue class
    # Function to Display
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
            current_node = current_node.next  # Traversing Node till last


def prime(number):
    lst = []
    # number = int(input("Enter the number:-"))
    for num in range(1, number + 1):  # Her range is given as from start to end
        if num > 1:
            for loop in range(2, num):  # here loop start from 2 as this is a exception for Prime number
                if (num % loop) == 0:
                    break
            else:
                lst.append(num)

    return lst


def anagram(lst):
    anagram_list = []
    for outer_loop in lst:
        for inner_loop in lst:
            if outer_loop != inner_loop and (sorted(str(outer_loop)) == sorted(str(inner_loop))):  # Actually Elements
                # or string is checked and sorted in oreder
                anagram_list.append(outer_loop)
                break
    return anagram_list


def prime1(start, end):
    lst = []
    # number = int(input("Enter the number:-"))
    for num in range(start, end + 1):  # Her range is given as from start to end
        if num > 1:
            for loop in range(2, num):  # here loop start from 2 as this is a exception for Prime number
                if (num % loop) == 0:
                    break
            else:
                lst.append(num)
    # print(lst)
    return lst


def binomialCoeff(n, k):
    res = 1

    # Since C(n, k) = C(n, n-k)
    if k > n - k:
        k = n - k

        # Calculate value of [n*(n-1)*---*(n-k+1)] /
    # [k*(k-1)*---*1]
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)

    return res


# A Binomial coefficient based function to
# find nth catalan number in O(n) time
def catalan(n):
    # Calculate value of 2nCn
    c = binomialCoeff(2 * n, n)

    # return 2nCn/(n+1)
    return c // (n + 1)


# A function to count number of BST
# with n nodes using catalan
def countBST(n):
    # find nth catalan number
    count = catalan(n)

    # return nth catalan number
    return count


# # A function to count number of binary
# # trees with n nodes
# def countBT(n):
#     # find count of BST with n numbers
#     count = catalan(n)
#
#     # return count * n!
#     return count * factorial(n)


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i  # To get a factorial of a number
    return res


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
        self.enqueue(amount)
        return balance

