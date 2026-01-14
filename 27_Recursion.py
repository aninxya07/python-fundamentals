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


# Tricky example to remember
def f(n):
    return f(n-1)

print(f(5))    # maybe it seems to go for an infinite loop

# But Python recursion doesn’t loop forever
# It hits the maximum recursion depth
# Then it throws, RecursionError: maximum recursion depth exceeded