from datastructure.Utility import Queue
import random


def main():
    while True:
        my_queue = Queue()
        try:
            panel = int(input("Enter the panel:-"))
            if panel > 10:
                print("Enter the Number of panel Between 1 to 10")
                # break
            hold = random.randint(1, panel)
            balance = 0
            for loop in range(hold + 1):
                my_queue.enqueue(loop + 1)
                print(loop + 1)
                # while True:
                choice = int(input("Enter your choice:-\n1.Withdraw Cash \n2.Deposit Cash"))
                if choice == 1:
                    balance = my_queue.withdraw(balance)
                    print("Balance after withdraw:", balance)
                elif choice == 2:
                    balance = my_queue.deposit(balance)
                    print("balance after deposit:", balance)
                else:
                    if my_queue.size == 0:
                        print("Queue is Empty")
        except ValueError:
            print("Sorry..!!!Invalid Input")

if __name__ == '__main__':
    main()
