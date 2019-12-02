from datastructure.Utility import prime1, anagram


def main():
    while True:
        try:
            start = int(input("Enter start of the number:- "))
            end = int(input("Enter End of the number:- "))
            if start > 1000:
                print("Sorry..!! Number should be less than 1000")
                break
            # for i in range(0, 10):
            prime = prime1(start, end)
            ana = anagram(prime)
            print(f"Anagram number in between {start} to {end}")
            print(ana)
            # start = start + 100
            # end = end + 100
        except ValueError:
            print("Sorry....!!! Invalid Input")


if __name__ == '__main__':
    main()
