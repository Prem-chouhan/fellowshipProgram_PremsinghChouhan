# A function to find factorial of a given number  
def factorial(n):
    res = 1

    # Calculate value of [1*(2)*---* 
    # (n-k+1)] / [k*(k-1)*---*1]
    for i in range(1, n + 1):
        res *= i
    return res



