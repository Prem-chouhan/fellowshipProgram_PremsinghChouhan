from datastructure.Utility import prime1


def main():
    while True:
        try:

            start = int(input("Enter start of the number:- "))
            end = int(input("Enter End of the number:- "))
    # for i in range(0, 10):
            prime_num = prime1(start, end)
            print(f"Prime number in between {start} to {end}")
            print(prime_num)
            # start = start + 100
            # end = end + 100

        except ValueError:
            print("Sorry....!!! Invalid Input")


if __name__ == '__main__':
    main()
