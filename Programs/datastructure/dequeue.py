from datastructure.Utility import Dequeue, NodeDequeue


def main():

    while True:
        pal_string = input("Enter Arithmetic Expression :-")
        my_deq = Dequeue()
        length = len(pal_string)
        for loop in range(length):
            hold = NodeDequeue(pal_string[loop])
            my_deq.add_rear(hold)
        size_pal = my_deq.size()
        is_pal = False
        for loop in range(int(size_pal // 2)):
            if my_deq.remove_front() is my_deq.remove_rear():
                is_pal = True
            size_pal -= 1
        if is_pal is True:
            print("String is Palindrome")
        else:
            print("String is NOT palindrome")


if __name__ == '__main__':
    main()
