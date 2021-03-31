from functools import lru_cache

# O(2^n) Time


def fibonacci_slow(n):
    if n in [0, 1]:
        return n
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)

# O(n) Time


@lru_cache(maxsize=1000)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# ~ O(n) Time
def fibonacci_optimized(n):
    cache = {}
    if n in cache:
        return cache[n]
    if n < 0:
        # edge case where n is negative
        raise ValueError("Index negative")

    elif n in [0, 1]:
        return n

    result = fibonacci_optimized(n - 1) + fibonacci_optimized(n - 2)
    cache[n] = result
    return result
# bottom up approach
## O(n) time and O(1) space.
def fibonacci_bottom_up(n):

    # Compute the nth Fibonacci number

    if n<0:
        raise ValueError(' no such thing as a negative index in a series')
    
    if n in [0,1]:
        return n
    
    prev_prev = 0
    prev = 1
    
    # start building the serie from the bottom up 
    for _ in range(n-1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
        
    
    return current


"""
# Fibonacci Series using Dynamic Programming (bottom up)
def fibonacci(n):
     
    # Taking 1st two fibonacci nubers as 0 and 1
    f = [0, 1]
     
     
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

"""

"""
TODO: Fibonacci using Matrix multiplication => O(log(n))
"""
