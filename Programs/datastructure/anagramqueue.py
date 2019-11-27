from datastructure.Utility import prime, anagram, Queue


def main():
    flag = True
    while flag:

        try:

            prime_num = int(input("Enter the number:- "))
            if prime_num > 1000:
                print("Sorry..!Number should be less than 1000")
            my_queue = Queue()
            prime_num = prime(prime_num)

            lst = anagram(prime_num)

            for loop in range(0, len(lst)):
                my_queue.enqueue(lst[loop])
            print("Anagram in Queue are:-")

            for loop in range(0, len(lst)):
                hold = my_queue.de_queue()
                print(hold)

        except ValueError:
            print("Sorry...!Invalid Input")


if __name__ == '__main__':
    main()
