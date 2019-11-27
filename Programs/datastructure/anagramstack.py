from datastructure.Utility import Stack, prime, anagram


def ang(number):
    lst = []
    my_stack = Stack()
    prime_num = prime(number)
    lst = anagram(prime_num)

    for loop in range(0, len(lst)):
        my_stack.push(lst[loop])

    for loop in range(0, len(lst)):
        hold = my_stack.pop()
        print(hold)
        lst.append(hold)

    return lst


def main():
    flag = True
    while flag:

        try:
            value = True

            while value:
                number = int(input("Enter the number:-"))

                if number > 1000:
                    print("Enter a number Smaller than 1000")
                    value = True
                else:
                    value = False
                    result = ang(number)
                    print("anagram list ", result)

        except ValueError:
            print("Sorry..!Invalid Input")


if __name__ == '__main__':
    main()
