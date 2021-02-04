# change this with the function you would like to compute the integral
def f(x):
    return x ** 2 - 1


def integral(f, a=0, b=2):
    """
    We use rectangle method for that: The rectangle method (also called the midpoint rule) 
    is the simplest method in Mathematics used 
    to compute an approximation of a definite integral.

    :type f: function (returns int)
    :type a: int
    :type b: int
    :rtype: float
    """
    n = 10  # number of time we cut the segment [ab]
    h = ((b - a) / n)
    I = 0
    for i in range(n):
        I += f(a + h * (i + 1 / 2))

    return h*I


print(integral(f))
