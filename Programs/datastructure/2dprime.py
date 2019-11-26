from datastructure.Utility import prime1, anagram

def main():
   
    start = 0
    end = 100
    for i in range(0, 10):
        prime = prime1(start, end)
        print(f"Prime number in between {start} to {end}")
        print(prime)
        start = start + 100
        end = end + 100

if __name__ == '__main__':
    main()