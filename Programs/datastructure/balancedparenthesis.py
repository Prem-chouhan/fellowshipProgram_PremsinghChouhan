from datastructure.Utility import Stack


def bal_paren():
    str = input("Enter the Arithmetic Expression:-")
    arr = []
    my_stack = Stack()
    open_paren = 0
    close_paren = 0

    for loop in range(len(str)):
        my_stack.push(str[loop])
        if str[loop] == "(":
            open_paren += 1

        if str[loop] == ")":
            close_paren += 1
            top = my_stack.pop()

    if open_paren == close_paren:
        print("Expression is Balanced ")
    else:
        print("Expression is  NOT Balanced ")


bal_paren()
