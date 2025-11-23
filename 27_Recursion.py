def fact(n):
    # base case
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))


def fibonacci(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(8))