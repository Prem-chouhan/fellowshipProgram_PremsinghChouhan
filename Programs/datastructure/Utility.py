class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list():
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def add_first(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            tempNode = self.head
            self.head = newNode
            self.head.next = tempNode
            del tempNode

    def add_position(self, newNode, pos):
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == pos:
                newNode.next = currentNode
                previousNode.next = newNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def print_list(self):
        if self.head is None:
            print("List is Empty: ")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def delete_end(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def size(self):
        count = 0
        currentNode = self.head
        while currentNode is not None:
            currentNode = currentNode.next
            count += 1
        print("Size of a list is:", count)

    def isempty(self):
        if self.head is None:
            print("List is Empty:")
        else:
            print("List is not Empty: ")

    def search_item(self, newNode):
        traverseNode = self.head
        while traverseNode is not None:
            if traverseNode.data is newNode.data:
                x = 1
                break
            else:
                traverseNode = traverseNode.next
        if x is 1:
            print("Data is Found")
        else:
            print("Data is not Found")


l1 = linked_list()
print("1.Add node\n2.Add First\n3.Add node at position\n4.Delete node\n5.,\n "
      "6.Search node in list\n7.Find size of list\n8.Display list")
choice = int(input("Enter your choice: "))
while choice is not False:
    while choice is not 0:
        if choice == 1:
            var1 = Node(input("Enter a data to store: "))
            l1.insert(var1)
            break
        elif choice == 2:
            var1 = Node(input("Enter a data to store: "))
            l1.add_first(var1)
            break
        elif choice == 3:
            var1 = Node(input("Enter a data to store: "))
            l1.add_position(var1)
            break
        elif choice == 4:
            l1.delete_end()
            break
        elif choice == 5:
            break
        elif choice == 6:
            var1 = Node(input("Enter a data to search: "))
            l1.search_item(var1)
            break
        elif choice == 7:
            l1.size()
            break
        elif choice == 8:
            l1.print_list()
            break
    choice = input("Enter a choice: ")








