# A function to find factorial of a given number  
def factorial(n):
    res = 1

    # Calculate value of [1*(2)*---* 
    # (n-k+1)] / [k*(k-1)*---*1]
    for i in range(1, n + 1):
        res *= i
    return res


def binomialCoeff(n, k):
    res = 1

    # Since C(n, k) = C(n, n-k)  
    if k > n - k:
        k = n - k

        # Calculate value of [n*(n-1)*---*(n-k+1)] /
    # [k*(k-1)*---*1]  
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)

    return res


# A Binomial coefficient based function to
# find nth catalan number in O(n) time  
def catalan(n):
    # Calculate value of 2nCn
    c = binomialCoeff(2 * n, n)

    # return 2nCn/(n+1)  
    return c // (n + 1)


# A function to count number of BST
# with n nodes using catalan  
def countBST(n):
    # find nth catalan number
    count = catalan(n)

    # return nth catalan number  
    return count


# A function to count number of binary
# trees with n nodes  
def countBT(n):
    # find count of BST with n numbers
    count = catalan(n)

    # return count * n!  
    return count * factorial(n)


# Driver Code
def main():
    n = int(input("Enter the number"))

    # find count of BST and binary 
    # trees with n nodes  
    count1 = countBST(n)
    count2 = countBT(n)

    # print count of BST and binary trees with n nodes  
    print("Count of BST with", n, "nodes is", count1)
    print("Count of binary trees with", n,
          "nodes is", count2)


if __name__ == '__main__':
    main()