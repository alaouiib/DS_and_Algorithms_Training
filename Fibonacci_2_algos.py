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


"""
TODO: Fibonacci using Matrix multiplication => O(log(n))
"""
