from datastructure.Utility import Stack


def bal_paren():
    express = input("Enter the Arithmetic Expression:-")
    arr = []
    express = Stack()
    open_paren = 0
    close_paren = 0

    for loop in range(len(express)):
        express.push(express[loop])
        if express[loop] == "(":
            open_paren += 1

        if express[loop] == ")":
            close_paren += 1
            top = express.pop()

    if open_paren == close_paren:
        print("Expression is Balanced ")
    else:
        print("Expression is  NOT Balanced ")


bal_paren()
