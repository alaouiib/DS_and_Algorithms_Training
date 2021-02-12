def find_repeat(numbers):

    # Find a number that appears more than once
    # sort array => nlogn
    numbers.sort()
    # floor = 0, ceil = len(e) -1
    floor_i, ceil_i = 0, len(numbers)-1

    # while floor < ceil
    while(floor_i < ceil_i):
        # take element in half index
        guess_index = floor_i + ((ceil_i - floor_i) // 2)
        # check if e[hi+1] == e[hi] or e[hi-1] == e[hi] return e[hi]
        if(numbers[guess_index] == numbers[guess_index + 1] or numbers[guess_index] == numbers[guess_index - 1]):
            return numbers[guess_index]
        # else: e[ceil] - e[hi] == len(e[hi:]) ? ceil <- hi : floor <- hi
        elif((numbers[ceil_i] - numbers[guess_index]) == len(numbers[guess_index:])):
            ceil_i = guess_index
        else:
            floor_i = guess_index
    return numbers[floor_i]
