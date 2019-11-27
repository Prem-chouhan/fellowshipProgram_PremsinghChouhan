from datastructure.Utility import Stack


def bal_paren(arith_exp):
    my_stack = Stack()
    open_paren = 0
    close_paren = 0
    # tup = ("(", ")")

    for loop in range(len(arith_exp)):
        my_stack.push(arith_exp[loop])

        if arith_exp[loop] == "(":
            open_paren += 1

        if arith_exp[loop] == ")":
            close_paren += 1
            top = my_stack.pop()
    return open_paren, close_paren


def main():
    while True:
        arith_exp = input("Enter the Arithmetic Expression:-")
        open_hold, clo_hold = bal_paren(arith_exp)

        if open_hold == clo_hold:
            print("Expression is Balanced ")
        else:
            print("Expression is  NOT Balanced ")


if __name__ == '__main__':
    main()
