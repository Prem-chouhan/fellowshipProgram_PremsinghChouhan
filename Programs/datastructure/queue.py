from datastructure.Utility import Queue
# from datastructure.Utility import withdraw
# from datastructure.Utility import deposit
import random

panel = int(input("Enter the panel:-"))
hold = random.randint(0, panel)
balance = 0
q = Queue()
for loop in range(hold):
    q.enqueue(loop+1)
    print(loop)
    choice = int(input("Enter your choice:-\n1.Withdraw Cash \n2.Deposit Cash"))
    if choice == 1:
        balance = q.withdraw(balance)
        print("Balance after withdraw:", balance)
    elif choice == 2:
        balance = q.deposit(balance)
        print("balance after deposit:", balance)
    else:
        if q.size == 0:
            print("Queue is Empty")






