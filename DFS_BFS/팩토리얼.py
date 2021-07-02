def factorial_function(n):
    if n<1:
        return 1
    else:
        return n*factorial_function(n-1)
print(factorial_function(10))