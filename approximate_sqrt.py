# we will use Newton's method
# Idea => repeat: compute (Xn+1 = Xn - (f(Xn)/f'(Xn))) until reaching precision (epsilon)

def approximate_sqrt(n: int, epsilon=0.001) -> float:
    # initialise guess, good value = n/2 (to avoid being on the stationary point or on the other side of the actual sqrt.)
    # for more details: see https://youtu.be/K45mV2Mv-Ug
    guess = n/2
    while (guess**2 - n > epsilon):
        guess = (guess + n/guess)/2
    return guess


print(approximate_sqrt(10, 0.001))  # => 3.16233, Actual sqrt(10) = 3.1622
